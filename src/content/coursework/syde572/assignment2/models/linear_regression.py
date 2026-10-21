import numpy as np
from sklearn.metrics import root_mean_squared_error


class LinearRegression:
    '''
    Linear basis function regression fitted by least squares with the pseudo-inverse:

        w = pinv(Phi) @ y
    '''
    def __init__(self):
        self.w = None

    def design_matrix(self, X: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def fit(self, X: np.ndarray, y: np.ndarray):
        Phi = self.design_matrix(X)
        self.w = np.linalg.pinv(Phi) @ y
        return self

    def regularized_fit(self, X: np.ndarray, y: np.ndarray, lam: np.ndarray):
        Phi = self.design_matrix(X)
        A = Phi.T @ Phi + np.diag(lam)
        self.w = np.linalg.pinv(A) @ (Phi.T @ y)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.design_matrix(X) @ self.w

    def evaluate(self, X: np.ndarray, y: np.ndarray) -> float:
        return root_mean_squared_error(y, self.predict(X))
