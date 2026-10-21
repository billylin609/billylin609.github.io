---
title: "Assignment 2"
category: "Course"
group: "SYDE 572"
author: "Yuchen Lin"
date: 2026-10-19
summary: "Assignment 2 homework submission page"
---


## Problem Definition

Applying linear regression models that model the relationship between multiple
independent variables $x_1 \dots x_d$ and dependent variable $y$ using a linear
hypothesis, given $\{X, y\}$.

$$
\hat{y} = \Phi(X)^T w\tag{1}\label{eq:hypothesis}
$$

$\Phi$ is the design matrix of basis functions.

## Dataset

First, load the dataset as a data frame for processing. The loading code is
adapted from the scikit-learn sample.[^boston]

[^boston]: scikit-learn, `sklearn.datasets.load_boston`.
    <https://scikit-learn.org/1.1/modules/generated/sklearn.datasets.load_boston.html>

```python
def __init__(self, url: str, columns: Optional[list] = None):
  '''
  boston dataset loading code derived from:
  https://scikit-learn.org/1.1/modules/generated/sklearn.datasets.load_boston.html
  '''
  raw_df = pd.read_csv(url, sep=r"\s+", skiprows=22, header=None)
  data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
  target = raw_df.values[1::2, 2]
  self.df = pd.DataFrame(np.column_stack([data, target]), columns=columns)
```

## Part 1: Polynomial Basis Function

To solve the linear regression with basis function, the operations are broken
down into two steps. First is to generate $\phi$ using polynomial basis, with
monomials of a single variable only and no cross-terms.

$$
\phi(x) = \left[1,\; x_1, x_1^2, \dots, x_1^M,\; x_2, x_2^2, \dots, x_d^M\right]
\tag{2}\label{eq:basis}
$$

Note: I have introduced 1 in the design matrix as the bias column, so $w_0$ is
the intercept.

Step 2 is to compute the weight for each feature by least squares, solved with
the pseudo-inverse.

$$
w^{*} = \left(\Phi\Phi^T\right)^{-1}\Phi y = \left(\Phi^T\right)^{-} y
\tag{3}\label{eq:weights}
$$

```python
# Implementation for computing design matrix
N, d = X.shape
cols = [np.ones(N)] + [X[:, j]**k for j in range(d) for k in range(1, self.degree + 1)]
return np.column_stack(cols)

# Computing the model weight
Phi = self.design_matrix(X)
self.w = np.linalg.pinv(Phi) @ y

# Predict
return self.design_matrix(X) @ self.w

# Compute Metric
return root_mean_squared_error(y, self.predict(X))
```


### a) demo polynomial regression

```python
# Train Test Split Implementation
self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, train_size=train_size, shuffle=shuffle)

# Fit the model with polynomial degree 1-7
degrees = list(range(1, 8))
train_rms, test_rms = [], []
for degree in degrees:
    model = PolynomialBasis(degree).fit(X_train, y_train)
    train_rms.append(model.evaluate(X_train, y_train))
    test_rms.append(model.evaluate(X_test, y_test))
    print(f"degree {degree}: train RMS = {train_rms[-1]:.4f}, "
          f"test RMS = {test_rms[-1]:.4e}")
```

| Degree | Train RMS ($1000s) | Test RMS ($1000s) |
|:---:|---:|---:|
| 1 | 2.037 | 36.44 |
| 2 | 1.578 | 1,097.19 |
| 3 | 1.449 | 48,672.83 |
| 4 | 1.282 | 29,316,003.22 |
| 5 | 1.282 | 345,791,732.62 |
| 6 | 1.510 | 6,331,452.42 |
| 7 | 1.602 | 988,143.02 |

![Training and test RMS error for each polynomial degree](figs/polynomial_rms.png)

#### Discussion

The model fits the training data well but the test RMS is orders
of magnitude larger, growing with degree up to degree 5.

The input data is not normalized, so the high powers explode. The fitting using
higher order polynomials does not provide meaning prediction on the test dataset.

### b) Normalized degree 1 polynomial basis fitting


```python
# Normalizing the dataset over all 506 samples
scaler = MinMaxScaler().fit(X_all)
X_train_norm, X_test_norm = scaler.transform(X_train), scaler.transform(X_test)

# Fitting the regression model
model = PolynomialBasis(degree=1).fit(X_train_norm, y_train)
```

| Weight | Feature | Description | Normalized |
|:---:|:---|:---|---:|
| bias | — | intercept | 1.0792 |
| $w_0$ | CRIM | per capita crime rate by town | −307.4751 |
| $w_1$ | ZN | proportion of residential land zoned for lots over 25,000 sq.ft. | 0.5382 |
| $w_2$ | INDUS | proportion of non-retail business acres per town | −4.6043 |
| $w_3$ | CHAS | Charles River dummy variable (= 1 if tract bounds river; 0 otherwise) | 0.0000 |
| $w_4$ | NOX | nitric oxides concentration (parts per 10 million) | 10.4565 |
| $\mathbf{w_5}$ | **RM** | average number of rooms per dwelling | **44.8362** |
| $w_6$ | AGE | proportion of owner-occupied units built prior to 1940 | −7.6939 |
| $\mathbf{w_7}$ | **DIS** | weighted distances to five Boston employment centres | **0.0839** |
| $w_8$ | RAD | index of accessibility to radial highways | −3.2178 |
| $w_9$ | TAX | full-value property-tax rate per \$10,000 | −3.9981 |
| $w_{10}$ | PTRATIO | pupil-teacher ratio by town | 1.4528 |
| $w_{11}$ | B | $1000(B_k - 0.63)^2$ where $B_k$ is the proportion of blacks by town | 2.6353 |
| $w_{12}$ | LSTAT | % lower status of the population | 0.9506 |

The two features of interest are highlighted. The normalization constants are
taken from the whole dataset so that both splits map into $[0, 1]$, and the RMS
is identical before and after normalizing, confirming the transform does not
change the fit.

RM (feature #6, average number of rooms per dwelling) has a weight of 44.8362,
and DIS (feature #8, weighted distance to five Boston employment centres) a
weight of 0.0839, the smallest of any feature apart from CHAS. CHAS is exactly
0.0000 because it is constant over the 100 training samples, so it carries no
information for the fit.

### c) 1D Regression visualization

```python
# Input filter Feature #2 only
feature = 2
name = COLUMNS[feature]
x_train, x_test = X_train[:, [feature]], X_test[:, [feature]]

# Normalizing over all 506 samples
scaler_1d = MinMaxScaler().fit(X_all[:, [feature]])
x_train_norm = scaler_1d.transform(x_train)
x_test_norm = scaler_1d.transform(x_test)

# Polynomial Fitting
for degree in degrees:
    model = PolynomialBasis(degree).fit(x_train_norm, y_train)
    train_rms_1d = model.evaluate(x_train_norm, y_train)
    test_rms_1d = model.evaluate(x_test_norm, y_test)
```

![Degree 1 fit on INDUS: training split left, test split right](figs/poly1d_indus_degree1.png)

![Degree 6 fit on INDUS: training split left, test split right](figs/poly1d_indus_degree6.png)

As shown in the result, the first 100 samples carry only limited information
about the dataset. A low-order polynomial captures the broad trend and gives a
reasonable result (degree 1 test RMS 9.86), but a higher-order one overfits
those 100 samples: degree 6 drives the training RMS down to 4.21 while
diverging outside the range the training data covers, pushing the test RMS to
1,009.13.

