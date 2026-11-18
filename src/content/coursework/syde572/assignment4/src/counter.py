from collections import Counter
from collections.abc import Hashable, Iterable, Sequence


def word_freqs(docs: Iterable[Sequence[str]]) -> Counter:
  return Counter(w for doc in docs for w in doc)


def label_freqs(labels: Iterable[Hashable]) -> Counter:
  return Counter(labels)


def word_freqs_by_label(docs: Iterable[Sequence[str]],
                        labels: Iterable[Hashable]) -> dict[Hashable, Counter]:
  freqs: dict[Hashable, Counter] = {}
  for doc, label in zip(docs, labels):
    freqs.setdefault(label, Counter()).update(doc)
  return freqs