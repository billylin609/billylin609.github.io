import logging
from collections import Counter
from collections.abc import Hashable, Iterable, Sequence
from dataclasses import dataclass

import numpy as np

try:
  from .counter import label_freqs, word_freqs, word_freqs_by_label
except ImportError:  # run directly: python naive_bayer.py
  from counter import label_freqs, word_freqs, word_freqs_by_label

logger = logging.getLogger(__name__)


def smooth(freqs: Counter, vocab: Iterable[str]) -> dict[str, float]:
  # Laplace smoothing: P(w) = (count(w) + 1) / (total + |V|)
  vocab = list(dict.fromkeys(vocab))
  denom = sum(freqs.values()) + len(vocab)
  return {w: (freqs[w] + 1) / denom for w in vocab}


@dataclass
class NBModel:
  log_prior: dict[Hashable, float]
  log_likelihood: dict[Hashable, dict[str, float]]
  vocab: set[str]

  @property
  def labels(self) -> list[Hashable]:
    return list(self.log_prior)


def train_nb(documents: Sequence[Sequence[str]], labels: Sequence[Hashable]) -> NBModel:
  n_docs = len(labels)
  vocab = set(word_freqs(documents))
  by_label = word_freqs_by_label(documents, labels)

  log_prior = {y: float(np.log(n / n_docs)) for y, n in label_freqs(labels).items()}
  log_likelihood = {
    y: {w: float(np.log(p)) for w, p in smooth(by_label[y], vocab).items()}
    for y in log_prior
  }
  return NBModel(log_prior, log_likelihood, vocab)


def unknown_words(document: Sequence[str], model: NBModel) -> list[str]:
  return [w for w in document if w not in model.vocab]


def score_doc_label(document: Sequence[str], label: Hashable, model: NBModel) -> float:
  if label not in model.log_prior:
    raise ValueError(f"unknown label {label!r}; model labels are {model.labels}")
  unknown = unknown_words(document, model)
  if unknown:
    logger.warning("skipping %d word(s) not in vocabulary: %s", len(unknown), unknown)
  log_likelihood = model.log_likelihood[label]
  return model.log_prior[label] + sum(log_likelihood[w] for w in document if w in model.vocab)


def classify_nb(document: Sequence[str], model: NBModel) -> Hashable:
  '''
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


def classify_documents(docs: Iterable[Sequence[str]], model: NBModel) -> list[Hashable]:
  return [classify_nb(doc, model) for doc in docs]


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


if __name__ == "__main__":
  import doctest
  doctest.testmod()
