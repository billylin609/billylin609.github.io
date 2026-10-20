import numpy as np
import pandas as pd
from typing import Optional
from sklearn.model_selection import train_test_split

class DataLoader:
    '''
    Load the Boston housing dataset and split it into training and test sets.

    >>> COLUMNS = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS",
    ...            "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]
    >>> loader = DataLoader('http://lib.stat.cmu.edu/datasets/boston', COLUMNS)
    >>> loader.df.shape
    (506, 14)

    >>> loader.train_test_split(loader.drop("MEDV"), loader["MEDV"], 100, False)
    >>> X_train, y_train = loader.get_train()
    >>> X_test, y_test = loader.get_test()
    >>> X_train.shape, y_train.shape
    ((100, 13), (100,))
    >>> X_test.shape, y_test.shape
    ((406, 13), (406,))

    >>> float(X_train[0, 0]), float(y_train[0])
    (0.00632, 24.0)
    >>> float(X_test[0, 0]), float(y_test[0])
    (0.14866, 27.5)
    '''
    def __init__(self, url: str, columns: Optional[list] = None):
        '''
        boston dataset loading code derived from:
        https://scikit-learn.org/1.1/modules/generated/sklearn.datasets.load_boston.html
        '''
        raw_df = pd.read_csv(url, sep=r"\s+", skiprows=22, header=None)
        data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
        target = raw_df.values[1::2, 2]
        self.df = pd.DataFrame(np.column_stack([data, target]), columns=columns)

    def train_test_split(self, X, y, train_size, shuffle: bool):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, train_size=train_size, shuffle=shuffle)

    def __getitem__(self, key: str) -> np.ndarray:
        return self.df[key].to_numpy()

    def drop(self, key:str) -> np.ndarray:
        return self.df.drop(columns=key).to_numpy()

    def get_train(self):
        return self.X_train, self.y_train

    def get_test(self):
        return self.X_test, self.y_test



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
