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

Where `texts` is the text of each line, `labels` is the pos or neg label
of the line (mapped to `1` and `-1`), `categories` is the category each review 
belongs to, and `doc_ids` is just an identifier.

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
library. 80% of the data is used for training and 20% for testing.
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
                           shuffle=True)
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

- The model itself is hardcoded to pos and neg. `train_nb` takes the
  classes from whatever labels it is given.
  Only the data loader maps `pos` and `neg` to `1` and `-1`.
- Smoothing is implemented in the `smooth` function, which is called by
  `train_nb`, so the stored log likelihoods are already smoothed.

## Classifying New Document

The predictor implementation is in three steps. Using the information provided
in the assignment, the log function is used instead of multiplication. Both
methods works because log is monotonic, and the log method avoids
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
  >>> train, _ = SentimentDataLoader(path).load_all_shuffle()
  >>> model = train_nb([text.split() for text in train.texts], train.labels.tolist())
  >>> probs = sanity_check_1(model, ["great"])

  P(["great"], pos) and P(["great"], neg):

  >>> probs['great'][1] > probs['great'][-1]
  True
  '''
  return {w: {y: float(np.exp(score_doc_label([w], y, model))) for y in model.labels}
          for w in words}
```

With a very short sentence the probability is very small. For the one-word
document `["great"]`, the positive probability is about 0.0013 and the negative
probability is about 0.00054. The exact values depend on the random train/test
split, but over 20 random splits the positive probability always stayed in
0.00128–0.00135, inside the expected 0.001–0.002 range. Since the split is not
seeded, the doctest checks that pos > neg instead of exact values.

In the doctest, sanity check 2 is also performed:

```py
def sanity_check_2(model: NBModel,
                   document: Sequence[str] = ("a", "top-quality", "performance")
                   ) -> dict[Hashable, float]:
  '''
  >>> from pathlib import Path
  >>> from dataloader import SentimentDataLoader
  >>> path = Path(__file__).resolve().parent.parent / "data" / "all_sentiment_shuffled.txt"
  >>> train, _ = SentimentDataLoader(path).load_all_shuffle()
  >>> model = train_nb([text.split() for text in train.texts], train.labels.tolist())

  'top-quality' never appears in training; scoring does not crash:

  >>> scores = sanity_check_2(model, ['a', 'top-quality', 'performance'])
  >>> scores[1] > scores[-1]
  True
  '''
  return {y: score_doc_label(document, y, model) for y in model.labels}
```

The code does not panic after injecting the unknown word `top-quality`: it is
skipped (and a warning is logged), and both classes still get a finite log
score (about −12.84 for pos and −13.44 for neg, varying by about ±0.1 across
random splits). Positive always scores higher.

We then use the `max` function to evaluate the MAP condition and pick the more
likely class. A doctest is performed on the first 10 samples. Over 20 random
splits, the model got 1 to 3 of the 10 reviews wrong (1.5 on average). The 3rd
review, a negative book review that starts by praising the author, is always
predicted as positive. The 4th, 5th and 6th reviews are sometimes wrong
too, depending on the split. This shows the code is working. (Note: on average about 8
of these 10 reviews also land in the training split, so this is a functional
check, not a fair accuracy measurement. Because the split changes every run,
the doctest only checks that 10 valid labels come back.)

```py
def classify_nb(document: Sequence[str], model: NBModel) -> Hashable:
  '''
  Classify the first 10 reviews of the dataset with a model trained on the
  80% training split (random, unseeded):

  >>> from pathlib import Path
  >>> from dataloader import SentimentDataLoader
  >>> path = Path(__file__).resolve().parent.parent / "data" / "all_sentiment_shuffled.txt"
  >>> loader = SentimentDataLoader(path)
  >>> train, _ = loader.load_all_shuffle()
  >>> model = train_nb([text.split() for text in train.texts], train.labels.tolist())
  >>> first_10 = loader.first_10()

  >>> preds = [classify_nb(text.split(), model) for text in first_10.texts]
  >>> len(preds), set(preds) <= {1, -1}
  (10, True)
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
Naive Bayes model is implemented manually. Only the `train_test_split` of the
data and the accuracy metric use sklearn, for better readability.)

```py
def accuracy(true_labels: Sequence[Hashable], guessed_labels: Sequence[Hashable]) -> float:
  return float(accuracy_score(true_labels, guessed_labels))
```

The code implementation for both the model parameter estimation and the
classifier can be found here: [`naive_bayer.py`](https://github.com/billylin609/billylin609.github.io/blob/main/src/content/coursework/syde572/assignment4/src/naive_bayer.py),
and the accuracy metric here: [`metric.py`](https://github.com/billylin609/billylin609.github.io/blob/main/src/content/coursework/syde572/assignment4/src/metric.py).

### Result

The train/test split is random, so the accuracy changes slightly on
each run. Evaluating the pos/neg classifier over 20 random 80/20 splits gives:

| Set | Reviews | Mean accuracy | Std | Range |
|---|---|---|---|---|
| Train | 9531 | 0.9275 | 0.0023 | 0.9212–0.9325 |
| Test | 2383 | 0.8044 | 0.0081 | 0.7885–0.8170 |

## Error Analysis

Here are some examples of the misclassified cases. (Note: since the split is
random, the set of misclassified reviews changes from run to run. The analysis
below only uses the runs where the review is in the test split.)

```md
................my man did his ' thing once again............... . ...................big-ups 2 dave , soul music.................. . & all musicians who 've collaborated *that 's how it 's 2 be done ! * .....why must feeble-minded folks always feel that it 's always someone 's job 2 educate them , why ca n't they relax & allow them - selves 2 be entertained ? *i suppose those of you that did n't get it were expecting for it 2 be " just like " the chapelle show ? were you expecting 2 see " ashy larry all-up & through " ! " 2 see the fugees hit the stage @ 1 time + " dead prez " that was much more than enough 4 me , when lauryn song " killing me softly " i almost cried son ! " ****matter of fact jersey stand up ! ! ! ! **** ******listen be not deceived , 4 those of you that have not see it *please do n't be fooled see it 4 your self 2 decide ! if you are not scared 2 be entertained " dig-in " ! ! ! ! ***** ......it 's the roots , fugees , mosdef / black starr , jill scott , erykah , big daddy kane , kool g rap , cody chesnutt , & my brothers " d-e-a-d*p-r-e-z " . ! ! ! !
```

The ground truth is positive but it's labelled as a negative feedback.
The original sentence is hard to make sense of, and the model is relying on
snippets like `expecting`, `not`, `n't`, `did`, `fooled` and `?`. These are
close to how negative feedback is expressed (e.g. "not what I was expecting"). This review is predicted as negative every time it is in the test split.

```md
i have not had a chance to thoroughly review this product , but i was disappointed the calendar feature could not display the information i wanted especially since i had contacted customer service prior to purchasing the program and was assured it could be done
```

The ground truth is positive and it's labelled as negative feedback.
This sentence is also from the dataset (`software pos 874.txt`). It looks like
a complaint (`disappointed`, `could not`, `contacted customer service`), but in
the dataset it is labelled as a positive review. The labels most likely come
from the star rating rather than the text, so the reviewer probably gave a high
rating while only writing about the one feature that bothered them. In this
case the model's prediction actually matches the text, so the error comes from
the label, not the model.

```md
 this is an all around awesome product . i have had great experiences with the program , and use it very often as we use it to create our entire high school 's yearbook . anyone one who says it does n't have the basics is pretty much lying to you , it has anything you 'll ever need and more . the people who review this product poorly do so because they do n't know how to use everything in it . the only problem i 've ever had is learing everything you can do with it , otherwise it is perfect
```

The ground truth is positive and it's labelled as negative feedback.
This is because the user is defending the product against the bad reviews, and
this makes the model think that this is negative feedback. Words like `poorly`,
`lying`, `n't` and `problem` come from describing the other reviews and the one
small problem, and they cancel out `awesome`, `great` and `perfect`. The score
difference between pos and neg is close to 0, so this review is a borderline
case that flips between pos and neg depending on the split.
