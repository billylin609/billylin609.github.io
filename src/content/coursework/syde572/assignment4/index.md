---
title: "Assignment 4"
category: "Course"
group: "SYDE 572"
author: "Yuchen Lin"
date: 2026-11-17
summary: "Assignment 4 homework submission page"
---

## Reading Data

The dataset used in the assignment is in the following format:

```md
Line format:  <category> <pos|neg> <doc_id>.txt <review text>
```

After reading the format of the input, I use a slightly different implementation
than the one in the original assignment, for better compatibility with the
6-class classification in the optional section.

The dataset is then stored in a python `dataclass`:

```py
@dataclass
class SentimentData:
  texts: np.ndarray
  labels: np.ndarray
  categories: np.ndarray
  doc_ids: np.ndarray
```

Where `texts` is the review text of each line, `labels` is the pos or neg label
of the line (mapped to `1` and `-1`), `categories` is the category the review
comes from, and `doc_ids` is just an identifier.

The way to process the dataset is as follows:

```py
# Parse each line
category, label, doc, text = line.strip().split(maxsplit=3)
if label not in LABELS:
  raise ValueError(f"unknown label {label!r} in line: {line[:80]!r}")
return category, LABELS[label], int(doc.removesuffix(".txt")), text

# Process the whole dataset
rows = []
with self.path.open(encoding="utf-8") as f:
  for line in f:
    if not line.strip():
      continue
    rows.append(parse_line(line))
    if limit is not None and len(rows) >= limit:  # used by first_10 mode
      break
categories, labels, doc_ids, texts = zip(*rows) if rows else ([], [], [], [])
return SentimentData(texts=np.array(texts, dtype=object),
                     labels=np.array(labels, dtype=int),
                     categories=np.array(categories, dtype=object),
                     doc_ids=np.array(doc_ids, dtype=int))
```

The implementation for loading the data supports three modes. `first_10` mode
only loads the first 10 data points for quick testing. `load_all` mode loads
all the data. `load_all_shuffle` mode loads all the data, then shuffles and
splits the dataset by calling the `train_test_split` method from the `sklearn`
library. By default, 80% of the data is used for training and 20% for testing,
and the split is stratified so both sets keep the same pos/neg ratio.
(Note: the assignment solution does not use any sklearn method for the Naive Bayes
model implementation.)

```py
def first_10(self, n: int = 10) -> SentimentData:
  return self._read(limit=n)

def load_all(self) -> SentimentData:
  return self._read()

def load_all_shuffle(self, test_size: float = 0.2, random_state: int | None = None,
                     stratify: bool = True) -> tuple[SentimentData, SentimentData]:
  data = self.load_all()
  parts = train_test_split(data.texts, data.labels, data.categories, data.doc_ids,
                           test_size=test_size, random_state=random_state,
                           shuffle=True,
                           stratify=data.labels if stratify else None)
  # Split the test_train result 
  self.train = SentimentData(*parts[0::2])
  self.test = SentimentData(*parts[1::2]) 
  return self.train, self.test
```

Dataloader code is available here: [`dataloader.py`](https://github.com/billylin609/billylin609.github.io/blob/main/src/content/coursework/syde572/assignment4/src/dataloader.py)

## Model Parameter Estimation

From the lecture notes, the Bayes' rule is:

$$
P(c|d) = \frac{P(d|c)P(c)}{P(d)}
$$

Since we are doing the same computation on both the positive and the negative
case and we are maximizing, $P(d)$ is the same for every class, therefore it's
safe to drop the denominator.

$$
\begin{aligned}
c_{MAP} &= \underset{c \in C}{\operatorname{argmax}} \; P(c|d)
         = \underset{c \in C}{\operatorname{argmax}} \; \frac{P(d|c)P(c)}{P(d)} \\
        &= \underset{c \in C}{\operatorname{argmax}} \; P(d|c)P(c)
\end{aligned}
$$

and since our input is multiple words $x_1, \dots, x_n$, the model can be
rewritten as the following

$$
c_{MAP} = \underset{c \in C}{\operatorname{argmax}} \; P(x_1, \dots, x_n|c)P(c)
$$

The naive assumption introduces two important concepts:

- the order of the words does not matter (bag of words)
- the features (words) are independent given class $c$

Using the above assumptions, $P(x_1, \dots, x_n|c) = \prod_{i=1}^{n} P(x_i|c)$,
so we can rewrite the equation as

$$
c_{NB} = \underset{c \in C}{\operatorname{argmax}} \; P(c) \prod_{x \in X} P(x|c)
$$

In this section, we are going to estimate the model parameters. The first thing
is to use the `Counter` class provided in the Python `collections` library to
count the frequency of each word in each class, which is then used to compute
the likelihood of a word given the class.

The verbal explanation for the equation is

$$
posterior \propto likelihood \times prior
$$

where the posterior is the prediction result of the class given the sentence.
The likelihood is the probability of each independent word belonging to the
class (pos or neg), and the prior is the overall probability of the positive or
negative case. (It is $\propto$ instead of $=$ because we dropped the
denominator $P(d)$.)

The prior is the fraction of training documents with class $c$:

$$
P(c) = \frac{N_c}{N}
$$

The likelihood $P(x|c)$ is the fraction of words in class $c$ that are the
word $x$ (with smoothing, explained below).

Multiplying many small probabilities underflows to 0, so the model works with
log probabilities instead, which turns the product into a sum:

$$
c_{NB} = \underset{c \in C}{\operatorname{argmax}} \left[ \log P(c) + \sum_{x \in X} \log P(x|c) \right]
$$

Words that never appear in the training set are not in $V$, so they are skipped
when scoring.

```py
# Preprocessing (split each review into words to enable further processing)
return [text.split() for text in data.texts]

# Compute the frequency of each word
return Counter(w for doc in docs for w in doc)

# Compute the frequency of the pos and neg cases in the documents
return Counter(labels)

# Compute the occurrence of each word under the pos or neg label
freqs: dict[Hashable, Counter] = {}
for doc, label in zip(docs, labels):
  freqs.setdefault(label, Counter()).update(doc)
return freqs
```

Counter implementation can be found here: [`counter.py`](https://github.com/billylin609/billylin609.github.io/blob/main/src/content/coursework/syde572/assignment4/src/counter.py)

There is a problem: a zero probability cannot be conditioned away. For example,
if a word only exists in the positive class and not in the negative class, then
$P(x|neg) = 0$, so any review containing that word gets a negative probability
of exactly 0, no matter what the other words say. In addition to that, $\log(0)$
does not exist ($-\infty$). Therefore Laplace smoothing is used to deal with
this issue.

The idea is to convert the original equation

$$
P(x|c) = \frac{\text{count of } x \text{ in class } c}{\text{total count of words in class } c}
$$

into

$$
P(x|c) = \frac{\text{count of } x \text{ in class } c + 1}{\text{total count of words in class } c + |V|}
$$

where $|V|$ is the number of distinct words in the training set. Adding $|V|$ to
the denominator (one for every word that got $+1$) keeps the probabilities of
all words summing to 1.

The code implementation for computing the model parameters:

```py
# Data Class Implementation
@dataclass
class NBModel:
  log_prior: dict[Hashable, float]
  log_likelihood: dict[Hashable, dict[str, float]]
  vocab: set[str]

# Parameter Estimation
# Total number of review
n_docs = len(labels)
# frequency of each word
vocab = set(word_freqs(documents))
# Frequency of the word given the label
by_label = word_freqs_by_label(documents, labels)
# Compute the possibility of a positive case or a negative case
log_prior = {y: float(np.log(n / n_docs)) for y, n in label_freqs(labels).items()}

log_likelihood = {
  y: {w: float(np.log(p)) for w, p in smooth(by_label[y], vocab).items()}
  for y in log_prior
}
return NBModel(log_prior, log_likelihood, vocab)

# Laplace Smooth Implementation
def smooth(freqs: Counter, vocab: Iterable[str]) -> dict[str, float]:
  # Laplace smoothing: P(w) = (count(w) + 1) / (total + |V|)
  vocab = list(dict.fromkeys(vocab))
  denom = sum(freqs.values()) + len(vocab)
  return {w: (freqs[w] + 1) / denom for w in vocab}
```

Response to the two hints:

- The model itself is not hardcoded to pos and neg: `train_nb` takes the
  classes from whatever labels it is given, so it also works for the 6-class
  topic task. Only the data loader maps `pos` and `neg` to `1` and `-1`.
- Smoothing is implemented in the `smooth` function, which is called by
  `train_nb`, so the stored log likelihoods are already smoothed.

## Classifying New Document

The predictor implementation is in three steps. Using the information provided
in the assignment, the log function is used instead of multiplication. Both
methods pick the same class because log is monotonic, and the log method avoids
underflow and is easier for comparison. If a word is unknown, the word is
dropped and ignored in the calculation.

```py
def score_doc_label(document: Sequence[str], label: Hashable, model: NBModel) -> float:
  # Handle unknown label (Panic)
  if label not in model.log_prior:
    raise ValueError(f"unknown label {label!r}; model labels are {model.labels}")
  # Handle unknown word (Drop)
  unknown = unknown_words(document, model)
  if unknown:
    logger.warning("skipping %d word(s) not in vocabulary: %s", len(unknown), unknown)
  log_likelihood = model.log_likelihood[label]
  # All the values are log probabilities, so the product becomes a sum
  return model.log_prior[label] + sum(log_likelihood[w] for w in document if w in model.vocab)
```

In the doctest, sanity check 1 is performed:

```py
def sanity_check_1(model: NBModel, words: Sequence[str] = ("great", "bad")
                   ) -> dict[str, dict[Hashable, float]]:
  '''
  >>> from pathlib import Path
  >>> from dataloader import SentimentDataLoader
  >>> path = Path(__file__).resolve().parent.parent / "data" / "all_sentiment_shuffled.txt"
  >>> train, _ = SentimentDataLoader(path).load_all_shuffle(random_state=0)
  >>> model = train_nb([text.split() for text in train.texts], train.labels.tolist())
  >>> probs = sanity_check_1(model, ["great"])

  P(["great"], pos) and P(["great"], neg):

  >>> round(probs['great'][1], 6), round(probs['great'][-1], 6)
  (0.00132, 0.000545)
  '''
  return {w: {y: float(np.exp(score_doc_label([w], y, model))) for y in model.labels}
          for w in words}
```

With a very short sentence the probability is very small. For the one-word
document `["great"]`, the positive probability is 0.00132, which is in the
expected 0.001–0.002 range and higher than the negative probability of
0.000545, so "great" leans positive as expected.

In the doctest, sanity check 2 is also performed:

```py
def sanity_check_2(model: NBModel,
                   document: Sequence[str] = ("a", "top-quality", "performance")
                   ) -> dict[Hashable, float]:
  '''
  >>> from pathlib import Path
  >>> from dataloader import SentimentDataLoader
  >>> path = Path(__file__).resolve().parent.parent / "data" / "all_sentiment_shuffled.txt"
  >>> train, _ = SentimentDataLoader(path).load_all_shuffle(random_state=0)
  >>> model = train_nb([text.split() for text in train.texts], train.labels.tolist())

  'top-quality' never appears in training; scoring does not crash:

  >>> scores = sanity_check_2(model, ['a', 'top-quality', 'performance'])
  >>> round(scores[1], 4), round(scores[-1], 4)
  (-12.8395, -13.4662)
  '''
  return {y: score_doc_label(document, y, model) for y in model.labels}
```

The code does not panic after injecting the unknown word `top-quality`: it is
skipped (and a warning is logged), and both classes still get a finite log
score (−12.84 for pos and −13.47 for neg).

We then use the `max` function to evaluate the MAP condition and pick the more
likely class. A doctest is performed on the first 10 samples, and the error rate
of the prediction is $\frac{1}{10}$ (only the 3rd review, a negative book review
that starts by praising the author, is predicted as positive), which shows the
code is working. (Note: 9 of these 10 reviews are also in the training split, so
this is a functional check, not a fair accuracy measurement.)

```py
def classify_nb(document: Sequence[str], model: NBModel) -> Hashable:
  '''
  Classify the first 10 reviews of the dataset with a model trained on the
  80% training split (seed 0):

  >>> from pathlib import Path
  >>> from dataloader import SentimentDataLoader
  >>> path = Path(__file__).resolve().parent.parent / "data" / "all_sentiment_shuffled.txt"
  >>> loader = SentimentDataLoader(path)
  >>> train, _ = loader.load_all_shuffle(random_state=0)
  >>> model = train_nb([text.split() for text in train.texts], train.labels.tolist())
  >>> first_10 = loader.first_10()

  >>> [classify_nb(text.split(), model) for text in first_10.texts]
  [-1, -1, 1, 1, 1, -1, -1, 1, -1, 1]
  >>> first_10.labels.tolist()
  [-1, -1, -1, 1, 1, -1, -1, 1, -1, 1]
  '''
  return max(model.labels, key=lambda y: score_doc_label(document, y, model))
```

## Evaluating The Classifier

The model predictor is implemented by looping over all the reviews in the list:

```py
def classify_documents(docs: Iterable[Sequence[str]], model: NBModel) -> list[Hashable]:
  return [classify_nb(doc, model) for doc in docs]
```

The accuracy is implemented using `sklearn.metrics.accuracy_score`. (Note: the
Naive Bayes model is programmed manually; only the `train_test_split` of the
data and the accuracy metric use sklearn, for better readability.)

```py
def accuracy(true_labels: Sequence[Hashable], guessed_labels: Sequence[Hashable]) -> float:
  return float(accuracy_score(true_labels, guessed_labels))
```

The code implementation for both the model parameter estimation and the
classifier can be found here: [`naive_bayer.py`](https://github.com/billylin609/billylin609.github.io/blob/main/src/content/coursework/syde572/assignment4/src/naive_bayer.py),
and the accuracy metric here: [`metric.py`](https://github.com/billylin609/billylin609.github.io/blob/main/src/content/coursework/syde572/assignment4/src/metric.py).

### Result

Evaluating the pos/neg classifier trained on the 80% training split (seed 0) gives:

| Set | Reviews | Accuracy |
|---|---|---|
| Train | 9531 | 0.9268 |
| Test | 2383 | 0.8053 |

## Error Analysis

