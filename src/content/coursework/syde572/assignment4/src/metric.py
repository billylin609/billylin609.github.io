from collections.abc import Hashable, Sequence
from sklearn.metrics import accuracy_score


def accuracy(true_labels: Sequence[Hashable], guessed_labels: Sequence[Hashable]) -> float:
  return float(accuracy_score(true_labels, guessed_labels))
