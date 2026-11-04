---
title: "Assignment 3"
category: "Course"
group: "SYDE 572"
author: "Yuchen Lin"
date: 2026-11-03
summary: "Assignment 3 homework submission page"
---


## Part I: Solve PCA by Hand

# Part 1: PCA by Hand

## Dataset

| Sample | $x_1$ | $x_2$ |
|:---:|:---:|:---:|
| ① | $-2$ | $-1$ |
| ② | $-1$ | $0$ |
| ③ | $0$ | $1$ |
| ④ | $1$ | $2$ |
| ⑤ | $2$ | $3$ |

---

## Step 1: Compute the Mean Vector

$$
m_1 = \frac{1}{n}\sum x_1 = \frac{1}{5}\big((-2) + (-1) + 0 + 1 + 2\big) = 0
$$

$$
m_2 = \frac{1}{n}\sum x_2 = \frac{1}{5}\big((-1) + 0 + 1 + 2 + 3\big) = 1
$$

$$
\mathbf{m} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

---

## Step 2: Compute the Covariance Matrix

$$
\begin{aligned}
C_x &= E\left[(\mathbf{x}-\mathbf{m})(\mathbf{x}-\mathbf{m})^T\right] \\
&= E\left[\mathbf{x}\mathbf{x}^T\right] - E\left[\mathbf{x}\mathbf{m}^T\right] - E\left[\mathbf{m}\mathbf{x}^T\right] + E\left[\mathbf{m}\mathbf{m}^T\right] \\
&= E\left[\mathbf{x}\mathbf{x}^T\right] - \mathbf{m}\mathbf{m}^T - \mathbf{m}\mathbf{m}^T + \mathbf{m}\mathbf{m}^T \\
&= E\left[\mathbf{x}\mathbf{x}^T\right] - \mathbf{m}\mathbf{m}^T
\end{aligned}
$$

### Outer products $\mathbf{x}_i\mathbf{x}_i^T$

$$
\begin{bmatrix} -2 \\ -1 \end{bmatrix}\begin{bmatrix} -2 & -1 \end{bmatrix} = \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}
\qquad
\begin{bmatrix} -1 \\ 0 \end{bmatrix}\begin{bmatrix} -1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}
$$

$$
\begin{bmatrix} 0 \\ 1 \end{bmatrix}\begin{bmatrix} 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}
\qquad
\begin{bmatrix} 1 \\ 2 \end{bmatrix}\begin{bmatrix} 1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}
$$

$$
\begin{bmatrix} 2 \\ 3 \end{bmatrix}\begin{bmatrix} 2 & 3 \end{bmatrix} = \begin{bmatrix} 4 & 6 \\ 6 & 9 \end{bmatrix}
$$

$$
\sum_i \mathbf{x}_i\mathbf{x}_i^T = \begin{bmatrix} 10 & 10 \\ 10 & 15 \end{bmatrix}
\qquad\Rightarrow\qquad
E\left[\mathbf{x}\mathbf{x}^T\right] = \frac{1}{5}\begin{bmatrix} 10 & 10 \\ 10 & 15 \end{bmatrix} = \begin{bmatrix} 2 & 2 \\ 2 & 3 \end{bmatrix}
$$

### Subtract $\mathbf{m}\mathbf{m}^T$

$$
\begin{aligned}
C_x &= \begin{bmatrix} 2 & 2 \\ 2 & 3 \end{bmatrix} - \begin{bmatrix} 0 \\ 1 \end{bmatrix}\begin{bmatrix} 0 & 1 \end{bmatrix} \\
&= \begin{bmatrix} 2 & 2 \\ 2 & 3 \end{bmatrix} - \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} \\
&= \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}
\end{aligned}
$$

---

## Step 3: Compute the Eigenvalues and Eigenvectors

$$
\det(C_x - \lambda I) = 0
\qquad
\begin{vmatrix} 2-\lambda & 2 \\ 2 & 2-\lambda \end{vmatrix} = 0
$$

$$
\begin{aligned}
(2-\lambda)^2 - 4 &= 4 - 4\lambda + \lambda^2 - 4 \\
&= \lambda(\lambda - 4) = 0
\end{aligned}
$$

$$
\boxed{\lambda_1 = 4, \quad \lambda_2 = 0}
$$

The first principal component corresponds to the larger eigenvalue, $\lambda_1 = 4$.

### Eigenvector for $\lambda_1 = 4$

$$
\begin{bmatrix} -2 & 2 \\ 2 & -2 \end{bmatrix}\begin{bmatrix} a \\ b \end{bmatrix} = \mathbf{0}
\quad\Rightarrow\quad
-2a + 2b = 0
\quad\Rightarrow\quad
a = b
\quad\Rightarrow\quad
(1,\ 1)
$$

The second row ($2a - 2b = 0$) is redundant.

Normalize:

$$
\mathbf{e}_1 = \frac{1}{\sqrt{2}}(1,\ 1) = \left(\frac{1}{\sqrt{2}},\ \frac{1}{\sqrt{2}}\right)
$$

### Eigenvector for $\lambda_2 = 0$

$$
\begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}\begin{bmatrix} a \\ b \end{bmatrix} = \mathbf{0}
\quad\Rightarrow\quad
2a + 2b = 0
\quad\Rightarrow\quad
a = -b
\quad\Rightarrow\quad
(1,\ -1)
$$

Normalize:

$$
\mathbf{e}_2 = \left(\frac{1}{\sqrt{2}},\ -\frac{1}{\sqrt{2}}\right)
$$

---

## Step 4: Decorrelation Check

$$
A = \begin{bmatrix} \mathbf{e}_1^T \\ \mathbf{e}_2^T \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[4pt] \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}
$$

$$
C_y = A\,C_x\,A^T =
\begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[4pt] \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}
\begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}
\begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\[4pt] \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{bmatrix}
= \begin{bmatrix} 4 & 0 \\ 0 & 0 \end{bmatrix}
$$

$C_y$ is diagonal, so the transformed components are **uncorrelated**.

---

## Q1: First Principal Component

$$
\boxed{PC_1 = \mathbf{w}_1 = \left(\frac{1}{\sqrt{2}},\ \frac{1}{\sqrt{2}}\right) \approx (0.707,\ 0.707)}
$$

Only the first principal component is kept, since $\lambda_2 = 0 \ll \lambda_1 = 4$. The 1-D PCA representation therefore captures all of the variance.

---

## Q2: Reconstruction Error of $(3, 3)$

**Subtract the mean:**

$$
\mathbf{t}' = \mathbf{t} - \boldsymbol{\mu} = \begin{bmatrix} 3 \\ 3 \end{bmatrix} - \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}
$$

**Project onto $PC_1$:**

$$
y = \mathbf{w}_1^T\mathbf{t}' = \frac{1}{\sqrt{2}}\cdot 3 + \frac{1}{\sqrt{2}}\cdot 2 = \frac{5}{\sqrt{2}}
$$

**Reconstruct:**

$$
\mathbf{x}' = \mathbf{w}_1\, y = \begin{bmatrix} \frac{1}{\sqrt{2}} \\[4pt] \frac{1}{\sqrt{2}} \end{bmatrix}\cdot\frac{5}{\sqrt{2}} = \begin{bmatrix} \frac{5}{2} \\[4pt] \frac{5}{2} \end{bmatrix}
$$

**Error:**

$$
\mathbf{t}' - \mathbf{x}' = \begin{bmatrix} 3 \\ 2 \end{bmatrix} - \begin{bmatrix} \frac{5}{2} \\[4pt] \frac{5}{2} \end{bmatrix} = \begin{bmatrix} 0.5 \\ -0.5 \end{bmatrix}
$$

$$
\|\mathbf{t}' - \mathbf{x}'\|_2 = \sqrt{0.5^2 + (-0.5)^2} = \sqrt{0.5} = \frac{\sqrt{2}}{2}
$$

$$
\boxed{L_2 \text{ error} = \frac{\sqrt{2}}{2} \approx 0.707}
$$

---

## Q3: Reconstruction Error of $(3, 4)$

Apply the same procedure.

**Subtract the mean:**

$$
\mathbf{t}' = \begin{bmatrix} 3 \\ 4 \end{bmatrix} - \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 3 \\ 3 \end{bmatrix}
$$

**Project onto $PC_1$:**

$$
y = \mathbf{w}_1^T\mathbf{t}' = \frac{1}{\sqrt{2}}\cdot 3 + \frac{1}{\sqrt{2}}\cdot 3 = \frac{6}{\sqrt{2}}
$$

**Reconstruct:**

$$
\mathbf{x}' = \mathbf{w}_1\, y = \begin{bmatrix} \frac{1}{\sqrt{2}} \\[4pt] \frac{1}{\sqrt{2}} \end{bmatrix}\cdot\frac{6}{\sqrt{2}} = \begin{bmatrix} 3 \\ 3 \end{bmatrix}
$$

**Error:**

$$
\mathbf{t}' - \mathbf{x}' = \begin{bmatrix} 3 \\ 3 \end{bmatrix} - \begin{bmatrix} 3 \\ 3 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

$$
\|\mathbf{t}' - \mathbf{x}'\|_2 = \sqrt{0^2 + 0^2} = 0
$$

$$
\boxed{L_2 \text{ error} = 0}
$$

The point $(3, 4)$ lies exactly on the line $x_2 = x_1 + 1$ spanned by $PC_1$ through the mean, so it is reconstructed perfectly.