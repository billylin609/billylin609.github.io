import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
from pathlib import Path

def newton_raphson_step(x, y, init_guess, step):
  f = Polynomial(init_guess)
  j = np.vander(x, len(init_guess), increasing=True)
  residual = f(x) - y
  return init_guess - step * np.linalg.solve(j.T @ j, j.T @ residual)


def plot_fit(x, y, history, mses, method='method3', start='step_0.500'):
  pad = 0.1 * (x.max() - x.min())
  xs = np.linspace(x.min() - pad, x.max() + pad, 200)
  final = Polynomial(history[-1])

  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

  # iterates shaded light to dark - one hue, because epoch is a magnitude
  shades = plt.cm.Blues(np.linspace(0.25, 0.85, len(history)))
  for coeffs, shade in zip(history, shades):
    ax1.plot(xs, Polynomial(coeffs)(xs), color=shade, linewidth=1, zorder=1)
  ax1.plot(xs, final(xs), color='#eb6834', linewidth=2, zorder=3,
           label=f'final fit: {Polynomial(np.round(history[-1], 4))}')
  ax1.plot(x, y, 'o', color='#1a1a19', markersize=8, zorder=4, label='data')

  ax1.grid(True, color='#d8d8d4', linewidth=0.6)
  ax1.set_axisbelow(True)
  ax1.set_xlabel('x')
  ax1.set_ylabel('y')
  ax1.set_title(f'Degree {len(history[-1]) - 1} fit over '
                f'{len(history)} iterations')
  ax1.legend(loc='upper left', framealpha=0.9)

  ax2.plot(range(len(mses)), mses, color='#2a78d6', linewidth=2,
           marker='o', markersize=4)
  ax2.axhline(mses[-1], color='#eb6834', linewidth=1, linestyle='--')
  ax2.annotate(f'final MSE = {mses[-1]:.4f}', (len(mses) - 1, mses[-1]),
               textcoords='offset points', xytext=(-8, 10),
               ha='right', color='#52514e')

  ax2.grid(True, color='#d8d8d4', linewidth=0.6)
  ax2.set_axisbelow(True)
  ax2.set_xlabel('epoch')
  ax2.set_ylabel('MSE')
  ax2.set_title('Mean squared error per epoch')

  fig.tight_layout()
  out_dir = Path(__file__).parent / method
  out_dir.mkdir(exist_ok=True)
  out = out_dir / f'fig_fit_{start}.png'
  fig.savefig(out, dpi=150, bbox_inches='tight')
  plt.close(fig)
  print(f'Saved {out}')


x_0 = np.array([0., 2., 1., 3.])
y_0 = np.array([0.5, 3.5, 1.5, 7.5])
step = 1

for init_guess in (np.array([1., 1.]), np.array([1., 1., 1.]), np.array([1., 1., 1., 1.])):
  degree = len(init_guess) - 1
  x = init_guess
  history, mses = [], []
  print(f'\n\nDegree {degree} polynomial, step {step}')
  for i in range(100):
    next_x = newton_raphson_step(x_0, y_0, x, step)
    f = Polynomial(x)
    mse = np.mean((f(x_0) - y_0)**2)
    history.append(x)
    mses.append(mse)
    print(f'Epoch: {i:3d}, MSE: {mse:9.6f}, f(x) = {f}')
    if np.linalg.norm(next_x - x) < 1e-7:
      break
    else:
      x = next_x
  print(f'Summary: degree {degree}, MSE {mses[-1]:.6f}, f(x) = '
        f'{Polynomial(np.round(history[-1], 4))}')
  plot_fit(x_0, y_0, history, mses, 'method3',
           f'degree_{degree}_step_{step:.3f}')
