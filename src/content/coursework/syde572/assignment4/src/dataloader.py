'''
Sentiment corpus loader.

Line format:  <category> <pos|neg> <doc_id>.txt <review text>
Labels:       pos -> 1, neg -> -1
Modes:        first_10          first 10 reviews
              load_all          all reviews, file order
              load_all_shuffle  all reviews, shuffled train/test split
'''
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from sklearn.model_selection import train_test_split

LABELS = {"pos": 1, "neg": -1}
MODES = ("first_10", "load_all", "load_all_shuffle")


@dataclass
class SentimentData:
  texts: np.ndarray
  labels: np.ndarray
  categories: np.ndarray
  doc_ids: np.ndarray

  def __len__(self) -> int:
    return len(self.labels)


def parse_line(line: str) -> tuple[str, int, int, str]:
  '''
  >>> parse_line("music neg 241.txt i bought this album .\\n")
  ('music', -1, 241, 'i bought this album .')
  >>> parse_line("books pos 278.txt a wonderful read")
  ('books', 1, 278, 'a wonderful read')
  >>> parse_line("books meh 1.txt hmm")
  Traceback (most recent call last):
      ...
  ValueError: unknown label 'meh' in line: 'books meh 1.txt hmm'
  '''
  category, label, doc, text = line.strip().split(maxsplit=3)
  if label not in LABELS:
    raise ValueError(f"unknown label {label!r} in line: {line[:80]!r}")
  return category, LABELS[label], int(doc.removesuffix(".txt")), text


class SentimentDataLoader:
  def __init__(self, path: str | Path):
    self.path = Path(path)
    self.train: SentimentData | None = None  # set by load_all_shuffle
    self.test: SentimentData | None = None

  def _read(self, limit: int | None = None) -> SentimentData:
    rows = []
    with self.path.open(encoding="utf-8") as f:
      for line in f:
        if not line.strip():
          continue
        rows.append(parse_line(line))
        if limit is not None and len(rows) >= limit:
          break
    categories, labels, doc_ids, texts = zip(*rows) if rows else ([], [], [], [])
    return SentimentData(texts=np.array(texts, dtype=object),
                         labels=np.array(labels, dtype=int),
                         categories=np.array(categories, dtype=object),
                         doc_ids=np.array(doc_ids, dtype=int))

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
    self.train = SentimentData(*parts[0::2])
    self.test = SentimentData(*parts[1::2])
    return self.train, self.test

  def load(self, mode: str = "load_all", **kwargs):
    if mode not in MODES:
      raise ValueError(f"mode must be one of {MODES}, got {mode!r}")
    return getattr(self, mode)(**kwargs)