import numpy as np
import pandas as pd


class DataLoader:
    '''
    Load the Iris dataset from the UCI repository.

    >>> URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    >>> COLUMNS = ["sepal length", "sepal width", "petal length", "petal width", "species"]
    >>> loader = DataLoader(URL, COLUMNS)
    >>> loader.df.shape
    (150, 5)

    >>> loader.drop("species").shape
    (150, 4)
    >>> loader["species"].shape
    (150,)

    >>> loader.df["species"].value_counts().to_dict()
    {'Iris-setosa': 50, 'Iris-versicolor': 50, 'Iris-virginica': 50}
    '''
    def __init__(self, url: str, columns: list):
        self.df = pd.read_csv(url, header=None, names=columns)

    def __getitem__(self, key: str) -> np.ndarray:
        return self.df[key].to_numpy()

    def drop(self, key: str) -> np.ndarray:
        return self.df.drop(columns=key).to_numpy()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
