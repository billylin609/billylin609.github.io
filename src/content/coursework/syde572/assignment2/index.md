---
title: "Assignment 2"
category: "Course"
group: "SYDE 572"
author: "Yuchen Lin"
date: 2026-10-19
summary: "Assignment 2 homework submission page"
---

# Dataset

## Part 1: Polynomial Basis Function

### a) Training and test error vs. polynomial degree

| Degree | Train RMS ($1000s) | Test RMS ($1000s) |
|:---:|---:|---:|
| 1 | 2.037 | 36.44 |
| 2 | 1.578 | 1,097.19 |
| 3 | 1.449 | 48,672.82 |
| 4 | 1.271 | 1.472 × 10¹⁵ |
| 5 | 1.097 | 1.092 × 10¹⁵ |
| 6 | 1.073 | 2.416 × 10¹⁴ |
| 7 | 0.882 | 6.862 × 10¹⁵ |

![Training and test RMS error vs. polynomial degree](figs/polynomial_rms.png)

### b) Learned weights for a degree 1 polynomial

% TODO: Understand standardization meaning here

| Weight | Feature | Description | Standardized | Original units |
|:---:|:---|:---|---:|---:|
| bias | — | intercept | 22.3090 | −37.9042 |
| $w_0$ | CRIM | per capita crime rate by town | −1.3380 | −3.4559 |
| $w_1$ | ZN | proportion of residential land zoned for lots over 25,000 sq.ft. | 0.1230 | 0.0054 |
| $w_2$ | INDUS | proportion of non-retail business acres per town | −0.5311 | −0.1688 |
| $w_3$ | CHAS | Charles River dummy variable (= 1 if tract bounds river; 0 otherwise) | 0.0000 | 0.0000 |
| $w_4$ | NOX | nitric oxides concentration (parts per 10 million) | 1.0027 | 21.5154 |
| $\mathbf{w_5}$ | **RM** | average number of rooms per dwelling | **4.1956** | **8.5910** |
| $w_6$ | AGE | proportion of owner-occupied units built prior to 1940 | −2.1663 | −0.0792 |
| $\mathbf{w_7}$ | **DIS** | weighted distances to five Boston employment centres | **0.0107** | **0.0076** |
| $w_8$ | RAD | index of accessibility to radial highways | −0.1938 | −0.1399 |
| $w_9$ | TAX | full-value property-tax rate per \$10,000 | −0.3486 | −0.0076 |
| $w_{10}$ | PTRATIO | pupil-teacher ratio by town | 0.2613 | 0.1546 |
| $w_{11}$ | B | $1000(B_k - 0.63)^2$ where $B_k$ is the proportion of blacks by town | 0.1811 | 0.0066 |
| $w_{12}$ | LSTAT | % lower status of the population | 0.1488 | 0.0262 |