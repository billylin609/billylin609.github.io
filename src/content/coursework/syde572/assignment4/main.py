import logging
from pathlib import Path

from src.dataloader import SentimentDataLoader
from src.metric import accuracy
from src.naive_bayer import classify_documents, train_nb

DATA_PATH = Path(__file__).resolve().parent / "data" / "all_sentiment_shuffled.txt"
LOG_PATH = Path(__file__).resolve().parent / "results" / "unknown_words.log"


def main():
  # Write the unknown-word warnings to a log file instead of the screen.
  logging.basicConfig(filename=LOG_PATH, filemode="w", format="%(message)s")

  # Load and split the data (80% train / 20% test)
  train, test = SentimentDataLoader(DATA_PATH).load_all_shuffle(random_state=0)
  train_docs = [text.split() for text in train.texts]
  test_docs = [text.split() for text in test.texts]

  # Train and evaluate
  model = train_nb(train_docs, train.labels.tolist())
  train_acc = accuracy(train.labels.tolist(), classify_documents(train_docs, model))
  test_acc = accuracy(test.labels.tolist(), classify_documents(test_docs, model))

  print(f"Train: {len(train)} reviews, accuracy {train_acc:.4f}")
  print(f"Test:  {len(test)} reviews, accuracy {test_acc:.4f}")


if __name__ == "__main__":
  main()
