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
        '''
        Basis function expansion X -> Phi, defined by each child class.
        X: (N, d) -> Phi: (N, M)
        '''
        raise NotImplementedError

    def fit(self, X: np.ndarray, y: np.ndarray):
        '''
        Solve for the weights w = pinv(Phi) @ y and store them in self.w.
        X: (N, d), y: (N,). Returns self so calls can be chained.

        pinv still works when Phi is rank-deficient (e.g. CHAS is all 0 in the
        training set), where (Phi^T Phi)^-1 does not exist.
        '''
        Phi = self.design_matrix(X)
        self.w = np.linalg.pinv(Phi) @ y
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        '''
        y_hat = Phi @ w.
        X: (N, d) -> y_hat: (N,)
        '''
        return self.design_matrix(X) @ self.w

    def evaluate(self, X: np.ndarray, y: np.ndarray) -> float:
        '''RMS error between y and predict(X), using root_mean_squared_error.'''
        return root_mean_squared_error(y, self.predict(X))
