import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
from pathlib import Path


def _save(fig, name, method='method4'):
  out_dir = Path(__file__).parent / method
  out_dir.mkdir(exist_ok=True)
  out = out_dir / f'{name}.png'
  fig.savefig(out, dpi=150, bbox_inches='tight')
  plt.close(fig)
  print(f'Saved {out}')

def _axes(x, y):
  '''A figure with the data points already drawn and the grid styled.'''
  fig, ax = plt.subplots(figsize=(6, 4.5))
  ax.plot(x, y, 'o', color='#1a1a19', markersize=8, zorder=4, label='data')
  ax.grid(True, color='#d8d8d4', linewidth=0.6)
  ax.set_axisbelow(True)
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  return fig, ax

def plot_final(x, y, history, mses, label):
  '''The converged fit against the data.'''
  pad = 0.1 * (x.max() - x.min())
  xs = np.linspace(x.min() - pad, x.max() + pad, 200)
  final = Polynomial(history[-1])
  fig, ax = _axes(x, y)
  ax.plot(xs, final(xs), color='#eb6834', linewidth=2, zorder=3,
          label=f'{Polynomial(np.round(history[-1], 4))}')
  ax.set_title(f'{label}: final fit (MSE = {mses[-1]:.4f})')
  ax.legend(loc='upper left', framealpha=0.9)
  _save(fig, f'fig_{label}_final')

def plot_iterations(x, y, history, mses, label):
  '''Every iterate, shaded light to dark as the fit converges.'''
  pad = 0.1 * (x.max() - x.min())
  xs = np.linspace(x.min() - pad, x.max() + pad, 200)
  fig, ax = _axes(x, y)
  shades = plt.cm.Blues(np.linspace(0.25, 0.9, len(history)))
  for coeffs, shade in zip(history, shades):
    ax.plot(xs, Polynomial(coeffs)(xs), color=shade, linewidth=1, zorder=1)
  ax.plot(xs, Polynomial(history[-1])(xs), color='#eb6834', linewidth=2,
          zorder=3, label='final')
  ax.set_ylim(min(y.min(), 0) - 1, y.max() + 2)
  ax.set_title(f'{label}: all {len(history)} iterations')
  ax.legend(loc='upper left', framealpha=0.9)
  _save(fig, f'fig_{label}_iterations')

def plot_mse(history, mses, label):
  '''MSE against epoch.'''
  fig, ax = plt.subplots(figsize=(6, 4.5))
  ax.plot(range(len(mses)), mses, color='#2a78d6', linewidth=2)
  ax.axhline(mses[-1], color='#eb6834', linewidth=1, linestyle='--')
  ax.annotate(f'final MSE = {mses[-1]:.4f}', (len(mses) - 1, mses[-1]),
              textcoords='offset points', xytext=(-8, 10), ha='right',
              color='#52514e')
  ax.grid(True, color='#d8d8d4', linewidth=0.6)
  ax.set_axisbelow(True)
  ax.set_xlabel('epoch')
  ax.set_ylabel('MSE')
  ax.set_title(f'{label}: mean squared error per epoch')
  _save(fig, f'fig_{label}_mse')

def plot_all(x, y, history, mses, label):
  '''The three figures for one fit, saved independently.'''
  plot_final(x, y, history, mses, label)
  plot_iterations(x, y, history, mses, label)
  plot_mse(history, mses, label)


def line_fitting(x, y, initial_guess, dm, ddm, db, ddb, tolerance=1e-7, max_iter=1000):
  m, b = initial_guess
  history, mses = [], []
  for i in range(max_iter):
    m_new = m - dm(m, b)/ddm(m, b)
    b_new = b - db(m_new, b)/ddb(m_new, b)
    step = np.linalg.norm([m_new - m, b_new - b])
    mse = np.mean((m_new*x + b_new - y)**2)
    history.append(np.array([b_new, m_new]))
    mses.append(mse)
    if i <= 2:
      print(f'epoch: {i}, m: {m_new:.6f}, b: {b_new:.6f}, '
            f'norm: {step:.3e}, MSE: {mse:.6f}')
    m = m_new
    b = b_new
    if step < tolerance:
      break
  print(f'Result: y = {m:.4f}x + {b:.4f}, '
        f'MSE = {np.mean((m*x + b - y)**2):.6f}')
  return m, b, history, mses

def parabola_fitting(x, y, initial_guess, da, dda, db, ddb, dc, ddc,
    tolerance=1e-7, max_iter=1000):
  a, b, c = initial_guess
  history, mses = [], []
  for i in range(max_iter):
    a_new = a - da(a, b, c)/dda(a, b, c)
    b_new = b - db(a_new, b, c)/ddb(a_new, b, c)
    c_new = c - dc(a_new, b_new, c)/ddc(a_new, b_new, c)
    step = np.linalg.norm([a_new - a, b_new - b, c_new - c])
    mse = np.mean((a_new*x**2 + b_new*x + c_new - y)**2)
    history.append(np.array([c_new, b_new, a_new]))
    mses.append(mse)
    if i <= 2:
      print(f'epoch: {i}, a: {a_new:.6f}, b: {b_new:.6f}, c: {c_new:.6f}, '
            f'norm: {step:.3e}, MSE: {mse:.6f}')
    a = a_new
    b = b_new
    c = c_new
    if step < tolerance:
      break
  print(f'Result: y = {a:.4f}x^2 + {b:.4f}x + {c:.4f}, '
        f'MSE = {np.mean((a*x**2 + b*x + c - y)**2):.6f}')
  return a, b, c, history, mses

x_0 = np.array([0., 2., 1., 3.])
y_0 = np.array([0.5, 3.5, 1.5, 7.5])

initial_guess = (1., 1.)

# D(m, b) = sum (m*x + b - y)^2, differentiated once and twice in each
# parameter separately
residual = lambda m, b: m*x_0 + b - y_0
dm  = lambda m, b: 2 * np.sum(x_0 * residual(m, b))
ddm = lambda m, b: 2 * np.sum(x_0**2)
db  = lambda m, b: 2 * np.sum(residual(m, b))
ddb = lambda m, b: 2 * len(x_0)

m, b, line_hist, line_mses = line_fitting(
    x_0, y_0, initial_guess, dm, ddm, db, ddb)
plot_all(x_0, y_0, line_hist, line_mses, 'line')

# D(a, b, c) = sum (a*x^2 + b*x + c - y)^2, same coordinate-wise scheme
parabola_initial_guess = (1., 1., 1.)
parabola_residual = lambda a, b, c: a*x_0**2 + b*x_0 + c - y_0
da  = lambda a, b, c: 2 * np.sum(x_0**2 * parabola_residual(a, b, c))
dda = lambda a, b, c: 2 * np.sum(x_0**4)
db2 = lambda a, b, c: 2 * np.sum(x_0 * parabola_residual(a, b, c))
ddb2 = lambda a, b, c: 2 * np.sum(x_0**2)
dc  = lambda a, b, c: 2 * np.sum(parabola_residual(a, b, c))
ddc = lambda a, b, c: 2 * len(x_0)

a, b, c, par_hist, par_mses = parabola_fitting(
    x_0, y_0, parabola_initial_guess, da, dda, db2, ddb2, dc, ddc)
plot_all(x_0, y_0, par_hist, par_mses, 'parabola')