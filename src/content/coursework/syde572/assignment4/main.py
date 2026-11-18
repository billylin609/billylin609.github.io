import argparse
import logging
from collections import Counter
from pathlib import Path

import numpy as np

from src.dataloader import MODES, SentimentData, SentimentDataLoader
from src.metric import accuracy
from src.naive_bayer import (NBModel, classify_documents, score_doc_label, train_nb,
                             unknown_words)

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "all_sentiment_shuffled.txt"
RESULTS_DIR = ROOT / "results"
LABEL_NAMES = {1: "pos", -1: "neg"}


def tokenize(data: SentimentData) -> list[list[str]]:
  return [text.split() for text in data.texts]


def write_misclassified(path: Path, test: SentimentData, docs: list[list[str]],
                        guesses: list, model: NBModel):
  '''
  Every wrong test prediction, grouped by true class; within a class the most
  confidently wrong come first.
  '''
  labels = test.labels.tolist()
  by_class: dict[int, list[tuple[float, int]]] = {y: [] for y in LABEL_NAMES}
  for i, (doc, true, guess) in enumerate(zip(docs, labels, guesses)):
    if guess != true:
      margin = score_doc_label(doc, guess, model) - score_doc_label(doc, true, model)
      by_class[true].append((margin, i))
  for wrong in by_class.values():
    wrong.sort(reverse=True)
  n_wrong = sum(len(w) for w in by_class.values())
  categories = sorted(set(test.categories.tolist()))

  lines = [
    "# Misclassified test reviews",
    "",
    f"{n_wrong} of {len(docs)} test reviews are wrong, grouped by true class. "
    "Within each class, sorted by margin = log P(doc, predicted) - log P(doc, true), "
    "largest (most confidently wrong) first.",
    "",
    "| true class | predicted | wrong | of | error rate |",
    "|---|---|---|---|---|",
  ]
  for y, name in LABEL_NAMES.items():
    total = labels.count(y)
    other = next(n for k, n in LABEL_NAMES.items() if k != y)
    lines.append(f"| {name} | {other} | {len(by_class[y])} | {total} | "
                 f"{len(by_class[y]) / total:.1%} |")

  lines += ["", "Errors per topic category:", "",
            "| category | " + " | ".join(f"true {n}" for n in LABEL_NAMES.values()) + " |",
            "|---|" + "---|" * len(LABEL_NAMES)]
  for cat in categories:
    counts = [sum(1 for _, i in by_class[y] if test.categories[i] == cat) for y in LABEL_NAMES]
    lines.append(f"| {cat} | " + " | ".join(map(str, counts)) + " |")
  lines.append("")

  for y, name in LABEL_NAMES.items():
    other = next(n for k, n in LABEL_NAMES.items() if k != y)
    lines += [f"# True {name}, predicted {other} ({len(by_class[y])} reviews)", ""]
    for rank, (margin, i) in enumerate(by_class[y], 1):
      lines += [
        f"## {name} {rank}. {test.categories[i]} {test.doc_ids[i]}.txt",
        "",
        f"margin {margin:.2f}, {len(docs[i])} words",
        "",
        f"> {test.texts[i]}",
        "",
      ]
  path.write_text("\n".join(lines), encoding="utf-8")
  return n_wrong


def write_unknown_words(path: Path, docs: list[list[str]], model: NBModel):
  '''Every test word that never appeared in training, with how often it occurs.'''
  counts = Counter(w for doc in docs for w in unknown_words(doc, model))
  n_tokens = sum(len(doc) for doc in docs)
  n_docs = sum(1 for doc in docs if unknown_words(doc, model))

  lines = [
    "# Test words not in the training vocabulary",
    "",
    f"- {len(counts)} distinct unknown words, {sum(counts.values())} occurrences "
    f"({sum(counts.values()) / n_tokens:.2%} of {n_tokens} test tokens)",
    f"- {n_docs} of {len(docs)} test reviews contain at least one unknown word",
    "- These words are skipped when scoring.",
    "",
    "| word | count |",
    "|---|---|",
  ]
  # unicode_escape makes hidden control characters visible (e.g. "the\x1a")
  lines += [f"| `{w.encode('unicode_escape').decode('ascii')}` | {c} |"
            for w, c in counts.most_common()]
  path.write_text("\n".join(lines) + "\n", encoding="utf-8")
  return len(counts)


def run_naive_bayes(train: SentimentData, test: SentimentData):
  # Unknown words are collected into a report instead of warning once per review.
  logging.getLogger("src.naive_bayer").setLevel(logging.ERROR)

  train_docs, test_docs = tokenize(train), tokenize(test)
  model = train_nb(train_docs, train.labels.tolist())

  train_guess = classify_documents(train_docs, model)
  test_guess = classify_documents(test_docs, model)
  print(f"Naive Bayes accuracy: "
        f"train {accuracy(train.labels.tolist(), train_guess):.4f}, "
        f"test {accuracy(test.labels.tolist(), test_guess):.4f}")

  RESULTS_DIR.mkdir(exist_ok=True)
  n_wrong = write_misclassified(RESULTS_DIR / "misclassified.md", test, test_docs,
                                test_guess, model)
  n_unknown = write_unknown_words(RESULTS_DIR / "unknown_words.md", test_docs, model)
  print(f"wrote {n_wrong} misclassified reviews to {RESULTS_DIR / 'misclassified.md'}")
  print(f"wrote {n_unknown} unknown words to {RESULTS_DIR / 'unknown_words.md'}")
  return model


def main():
  parser = argparse.ArgumentParser(description="Load the sentiment corpus.")
  parser.add_argument("--mode", choices=MODES, default="first_10",
                      help="first_10: first N reviews, load_all: every review, "
                           "load_all_shuffle: shuffled split + naive Bayes")
  parser.add_argument("-n", type=int, default=10, help="reviews to load in first_10 mode")
  parser.add_argument("--test-size", type=float, default=0.2)
  parser.add_argument("--seed", type=int, default=0)
  args = parser.parse_args()

  loader = SentimentDataLoader(DATA_PATH)

  if args.mode == "first_10":
    data = loader.first_10(n=args.n)
    for label, cat, doc_id, text in zip(data.labels, data.categories,
                                        data.doc_ids, data.texts):
      print(f"  {label:+d}  {cat:<8} {doc_id:>5}  {text[:70]}...")
  elif args.mode == "load_all":
    pass
  else:
    loader.load_all_shuffle(test_size=args.test_size, random_state=args.seed)
    run_naive_bayes(loader.train, loader.test)


if __name__ == "__main__":
  main()
