import numpy as np
import matplotlib.pyplot as plt
from typing import Callable
from pathlib import Path

# Represent the equation
def newton_polynomial(x0, y0, f, df, ddf,
    initial_guess=0.0, tolerance=1e-7, max_iter=100):
  '''
  Newton-Raphson Method to Approx. shortest distance
  from a point to a function.

  Minimizes the squared distance
  D(x) = (x - x0)^2 + (f(x) - y0)^2
  by driving D'(x) to zero.

  @Input:
  x0: float the x coordinate of the point
  y0: float the y coordinate of the point
  f: lambda
  df: lambda first order derivative
  ddf: lambda second order derivative.
  initial_guess: float the starting x for the iteration
  tolerance: float stop once the step is smaller than this

  @return:
  x: the closest point
  '''
  print(f'\nPoint: ({x0:.3f}, {y0:.3f}), Initial Guess: {initial_guess:.3f}')
  x = initial_guess
  for i in range(max_iter):
    if i < 5:
      verbose = True
    else:
      verbose = False
    next_x = newton_step(x0, y0, f(x), df(x), ddf(x),
                x, verbose)
    converged = abs(next_x - x) < tolerance
    x = next_x
    print(f'Epoch: {i}, x: {x}, Distance: {distance(x, x0, f(x), y0):.3f}')
    if converged:
      break
  return x

def newton_step(x0, y0, f, df, ddf, x,
    verbose=False):
  D_prime = 2*(x-x0) + 2 * (f-y0)*df
  D_double_prime = 2 + 2*(df**2) + 2*(f-y0)*ddf
  next_x = x - D_prime/D_double_prime
  if verbose == True:
    print(f'Guess:{x:.5f}, D\'{D_prime:.3f}, D\'\'{D_double_prime:.3f}, '
          f'Next_Guess:{next_x:.3f}')
  return next_x

def distance(x, x0, f, y0):
  '''
  Compute the shortest distance from a function to a point
  '''
  return np.sqrt((x-x0)**2+(f-y0)**2)

def plot(x: float, x0: float, f: Callable, y0: float, method: str, start: str):
  '''
  Plot the curve, the query point, and the segment joining them.

  @Input:
  x: float the closest point on the curve, from newton_polynomial
  x0: float the x coordinate of the point
  f: callable the function that was minimised against
  y0: float the y coordinate of the point
  method: str the method folder the figure is saved under, e.g. 'method1'
  start: str the starting condition, e.g. 'init_1.000', used in the name
  '''
  d = distance(x, x0, f(x), y0)

  # frame a square window around both points, so equal aspect stays readable
  half = max(d * 1.4, 2.5)   # keep enough curve in frame when d is tiny
  cx, cy = (x0 + x) / 2, (y0 + f(x)) / 2
  xs = np.linspace(cx - half, cx + half, 400)

  fig, ax = plt.subplots(figsize=(6, 6))
  ax.plot(xs, f(xs), color='#2a78d6', linewidth=2, label='f(x)')
  ax.plot([x0, x], [y0, f(x)], color='#eb6834', linewidth=2, linestyle='--',
          marker='o', markersize=8, label=f'shortest distance = {d:.3f}')
  ax.annotate(f'({x0:.3f}, {y0:.3f})', (x0, y0),
              textcoords='offset points', xytext=(14, -14), color='#52514e')
  ax.annotate(f'({x:.3f}, {f(x):.3f})', (x, f(x)),
              textcoords='offset points', xytext=(14, 8), color='#52514e')

  ax.set_xlim(cx - half, cx + half)
  ax.set_ylim(cy - half, cy + half)
  ax.set_aspect('equal')
  ax.grid(True, color='#d8d8d4', linewidth=0.6)
  ax.set_axisbelow(True)
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_title(f'Point ({x0:g}, {y0:g}), {start.replace("_", " ")}')
  ax.legend(loc='lower right', framealpha=0.9)

  out_dir = Path(__file__).parent / method
  out_dir.mkdir(exist_ok=True)
  out = out_dir / f'fig_point_{x0:.3f}_{y0:.3f}_{start}.png'
  fig.savefig(out, dpi=150, bbox_inches='tight')
  plt.close(fig)
  print(f'Saved {out}')

if __name__ == '__main__':
  f = lambda x: x**2+5

  points = ((0, 0), (-4, 0), (-8, 0), (2, 0), (6, 0))
  initial_guesses = (1, 0, 0, 0, 0)

  for (x0, y0), initial_guess in zip(points, initial_guesses):
    print(f'\n\n Points: ({x0}, {y0})')
    closest_x = newton_polynomial(x0=x0, y0=y0,
                      f=f,
                      df=lambda x: 2*x,
                      ddf=lambda x: 2*(x**0),
                      initial_guess=initial_guess)
    print(f'Summary: Best x: {closest_x:.4f}, '
          f'Distance: {distance(closest_x, x0, f(closest_x), y0):.4f}')
    plot(closest_x, x0, f, y0, 'method1', f'init_{initial_guess:.3f}')
