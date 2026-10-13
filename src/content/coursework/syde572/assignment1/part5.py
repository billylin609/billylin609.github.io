import io
import contextlib

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from part1 import newton_polynomial, newton_step, plot, distance

# part2 runs its driver at import time, so silence that one import.  The
# figures it rewrites are identical to the ones it already produced.
with contextlib.redirect_stdout(io.StringIO()):
  from part2 import golden_bisection, update_x1, update_x2

# Part 5: the point (2, 10) lies INSIDE the parabola, so the squared
# distance D(x) has two local minima.  Both methods are local: Newton
# follows whichever basin its initial guess falls in, and golden-section
# follows whichever minimum its bracket encloses.  The fix for both is to
# start from several places and keep the nearest result.

f = lambda x: x**2+5
df = lambda x: 2*x
ddf = lambda x: 2*np.ones_like(x)

def quiet(fn, *args, **kwargs):
  '''Call fn without its per-iteration printing.'''
  with contextlib.redirect_stdout(io.StringIO()):
    return fn(*args, **kwargs)


def plot_newton_steps(x0, y0, f, df, ddf, initial_guess, n_steps,
    method='method5', span=3.0):
  '''
  Show the Newton construction on D'(x): at each guess, the tangent whose
  slope is D''(x) is followed down to the axis, and that crossing is the
  next guess.

  @Input:
  initial_guess: float the starting x
  n_steps: int how many iterations to draw
  span: float half-width of the plotted window around the iterates
  '''
  D1 = lambda x: 2*(x - x0) + 2*(f(x) - y0)*df(x)
  D2 = lambda x: 2 + 2*df(x)**2 + 2*(f(x) - y0)*ddf(x)

  xk = initial_guess
  iterates = [xk]
  for _ in range(n_steps):
    xk = xk - D1(xk)/D2(xk)
    iterates.append(xk)

  lo = min(iterates) - span
  hi = max(iterates) + span
  xs = np.linspace(lo, hi, 400)
  ymax = max(abs(D1(np.array(iterates)))) * 1.3

  fig, ax = plt.subplots(figsize=(7, 4.5))
  ax.plot(xs, D1(xs), color='#2a78d6', linewidth=2, label="D'(x)")
  ax.axhline(0, color='#52514e', linewidth=1)

  shades = plt.cm.Oranges(np.linspace(0.45, 0.9, n_steps))
  for k in range(n_steps):
    a, b = iterates[k], iterates[k+1]
    # the tangent at (a, D'(a)) reaches zero exactly at the next guess
    ax.plot([a, b], [D1(a), 0], color=shades[k], linewidth=1.5, zorder=2)
    ax.plot([a, a], [0, D1(a)], color=shades[k], linewidth=0.8,
            linestyle=':', zorder=2)
    ax.plot(a, D1(a), 'o', color=shades[k], markersize=8, zorder=3)
    if k == 0 or abs(a - iterates[k-1]) > 0.05*(hi - lo):
      ax.annotate(f'$x_{k}$', (a, 0), textcoords='offset points',
                  xytext=(0, -16), ha='center', color='#52514e', fontsize=9)

  ax.plot(iterates[-1], D1(iterates[-1]), 'o', color='#1baf7a',
          markersize=9, zorder=4, label=f'x = {iterates[-1]:.4f}')
  ax.set_ylim(-ymax, ymax)
  ax.grid(True, color='#d8d8d4', linewidth=0.6)
  ax.set_axisbelow(True)
  ax.set_xlabel('x')
  ax.set_ylabel("D'(x)")
  ax.set_title(f"Newton-Raphson on $D'(x)$ from ({x0}, {y0}), "
               f"guess {initial_guess:g}")
  ax.legend(loc='best', framealpha=0.9)

  out_dir = Path(__file__).parent / method
  out_dir.mkdir(exist_ok=True)
  out = out_dir / f'fig_steps_point_{x0:.3f}_{y0:.3f}_init_{initial_guess:.3f}.png'
  fig.savefig(out, dpi=150, bbox_inches='tight')
  plt.close(fig)
  print(f'Saved {out}')

def plot_golden_intervals(x0, y0, f, a, b, n_iter, method='method5'):
  '''
  Show the bracket closing in.  Each row is one iteration: the bar spans
  [a, b] and the two markers are the interior points x1 and x2, one of
  which is carried over into the next row.
  '''
  phi = (1 + np.sqrt(5))/2
  resphi = 2 - phi
  D = lambda x: (x - x0)**2 + (f(x) - y0)**2

  x1, x2 = update_x1(a, b, resphi), update_x2(a, b, resphi)
  d1, d2 = D(x1), D(x2)
  rows = [(a, b, x1, x2)]
  for _ in range(n_iter):
    if d1 < d2:
      b, x2, d2 = x2, x1, d1
      x1 = update_x1(a, b, resphi); d1 = D(x1)
    else:
      a, x1, d1 = x1, x2, d2
      x2 = update_x2(a, b, resphi); d2 = D(x2)
    rows.append((a, b, x1, x2))

  lo, hi = rows[0][0], rows[0][1]
  fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 6), sharex=True,
                                 gridspec_kw={'height_ratios': [2, 3]})

  xs = np.linspace(lo, hi, 400)
  mid = (rows[-1][0] + rows[-1][1])/2
  ax1.plot(xs, D(xs), color='#2a78d6', linewidth=2, label='D(x)')
  ax1.plot(mid, D(mid), 'o', color='#1baf7a', markersize=9, zorder=3,
           label=f'x = {mid:.4f}')
  ax1.grid(True, color='#d8d8d4', linewidth=0.6)
  ax1.set_axisbelow(True)
  ax1.set_ylabel('D(x)')
  ax1.set_title(f'Golden-section bracket closing on ({x0}, {y0})')
  ax1.legend(loc='best', framealpha=0.9)

  for i, (ra, rb, rx1, rx2) in enumerate(rows):
    ax2.plot([ra, rb], [i, i], color='#2a78d6', linewidth=2.5,
             solid_capstyle='butt', zorder=2)
    ax2.plot([ra, rb], [i, i], '|', color='#2a78d6', markersize=12, zorder=3)
    ax2.plot(rx1, i, 'o', color='#eb6834', markersize=7, zorder=4)
    ax2.plot(rx2, i, 'o', color='#1baf7a', markersize=7, zorder=4)
    ax2.annotate(f'{rb - ra:.3f}', (rb, i), textcoords='offset points',
                 xytext=(8, -3), color='#52514e', fontsize=8)

  ax2.plot([], [], 'o', color='#eb6834', markersize=7, label='$x_1$')
  ax2.plot([], [], 'o', color='#1baf7a', markersize=7, label='$x_2$')
  ax2.invert_yaxis()
  ax2.set_yticks(range(len(rows)))
  ax2.set_ylabel('iteration')
  ax2.set_xlabel('x')
  ax2.grid(True, axis='x', color='#d8d8d4', linewidth=0.6)
  ax2.set_axisbelow(True)
  ax2.legend(loc='lower left', framealpha=0.9, fontsize=9)

  fig.tight_layout()
  out_dir = Path(__file__).parent / method
  out_dir.mkdir(exist_ok=True)
  out = out_dir / f'fig_intervals_point_{x0:.3f}_{y0:.3f}.png'
  fig.savefig(out, dpi=150, bbox_inches='tight')
  plt.close(fig)
  print(f'Saved {out}')


def multi_start_newton(x0, y0, f, df, ddf, initial_guesses, domain=None,
    verbose=True):
  '''
  Run Newton from every guess and keep the nearest result.

  @Input:
  domain: (lo, hi) or None, the interval f is defined on.  A guess that
    leaves it, or that diverges, is discarded rather than compared.

  @return:
  best_x: the closest point found
  best_guess: the guess that produced it
  '''
  best_x, best_guess, best_d = None, None, np.inf
  for guess in initial_guesses:
    with np.errstate(all='ignore'):
      x = quiet(newton_polynomial, x0, y0, f, df, ddf, guess)
      if not np.isfinite(x) or (domain and not domain[0] <= x <= domain[1]):
        if verbose:
          print(f'  newton guess {guess:+6.2f} -> left the domain, discarded')
        continue
      d = distance(x, x0, f(x), y0)
    if verbose:
      print(f'  newton guess {guess:+6.2f} -> x {x:+.4f}, distance {d:.4f}')
    if d < best_d:
      best_x, best_guess, best_d = x, guess, d
  return best_x, best_guess

def newton_iterates(x0, y0, f, df, ddf, initial_guess, n_steps):
  '''Run n_steps of Newton and return every intermediate guess.'''
  x = initial_guess
  xs = [x]
  for _ in range(n_steps):
    x = quiet(newton_step, x0, y0, f(x), df(x), ddf(x), x)
    xs.append(x)
  return xs

def plot_iterates(x0, y0, f, iterates, domain, label, method='method5'):
  '''Plot the first few Newton iterates marching toward the solution.'''
  lo, hi = domain
  xs = np.linspace(lo, hi, 400)
  fig, ax = plt.subplots(figsize=(6, 4.5))
  with np.errstate(all='ignore'):
    ax.plot(xs, f(xs), color='#2a78d6', linewidth=2, label=label)
  shades = plt.cm.Blues(np.linspace(0.3, 0.9, len(iterates)))
  last_labelled = None
  for k, (xk, shade) in enumerate(zip(iterates, shades)):
    ax.plot([x0, xk], [y0, f(xk)], color=shade, linewidth=1.2, zorder=2)
    ax.plot(xk, f(xk), 'o', color=shade, markersize=8, zorder=3)
    # once the iterates converge the labels sit on top of each other
    if last_labelled is None or abs(xk - last_labelled) > 0.04*(hi - lo):
      ax.annotate(str(k), (xk, f(xk)), textcoords='offset points',
                  xytext=(0, 10), ha='center', color='#52514e', fontsize=9)
      last_labelled = xk
  final = iterates[-1]
  d = distance(final, x0, f(final), y0)
  ax.plot([x0, final], [y0, f(final)], color='#eb6834', linewidth=2,
          zorder=4, label=f'converged, d = {d:.3f}')
  ax.plot(x0, y0, 'o', color='#1a1a19', markersize=9, zorder=5)
  ax.grid(True, color='#d8d8d4', linewidth=0.6)
  ax.set_axisbelow(True)
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_title(f'{label} - first {len(iterates)-1} Newton iterations')
  ax.legend(loc='best', framealpha=0.9, fontsize=9)
  out_dir = Path(__file__).parent / method
  out_dir.mkdir(exist_ok=True)
  out = out_dir / f'fig_{label.replace(" ", "_")}_iterates.png'
  fig.savefig(out, dpi=150, bbox_inches='tight')
  plt.close(fig)
  print(f'Saved {out}')

def plot_curve(x0, y0, f, best_x, domain, label, method='method5'):
  '''Plot a general curve, the query point and the shortest segment.'''
  lo, hi = domain
  xs = np.linspace(lo, hi, 400)
  d = distance(best_x, x0, f(best_x), y0)
  fig, ax = plt.subplots(figsize=(6, 4.5))
  with np.errstate(all='ignore'):
    ax.plot(xs, f(xs), color='#2a78d6', linewidth=2, label=label)
  ax.plot([x0, best_x], [y0, f(best_x)], color='#eb6834', linewidth=2,
          linestyle='--', marker='o', markersize=8,
          label=f'shortest distance = {d:.3f}')
  ax.plot(x0, y0, 'o', color='#1a1a19', markersize=9, zorder=5)
  ax.set_aspect('equal')
  ax.grid(True, color='#d8d8d4', linewidth=0.6)
  ax.set_axisbelow(True)
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_title(f'{label} - closest point to ({x0}, {y0})')
  ax.legend(loc='best', framealpha=0.9, fontsize=9)
  out_dir = Path(__file__).parent / method
  out_dir.mkdir(exist_ok=True)
  out = out_dir / f'fig_{label.replace(" ", "_")}_point_{x0:.3f}_{y0:.3f}.png'
  fig.savefig(out, dpi=150, bbox_inches='tight')
  plt.close(fig)
  print(f'Saved {out}')

def multi_bracket_golden(x0, y0, f, a, b, n_sub):
  '''
  Split [a, b] into n_sub sub-brackets and keep the nearest result.

  Golden-section only guarantees a minimum when the objective is
  unimodal on the bracket; narrow sub-brackets restore that property.

  @return:
  best_x: the closest point found
  best_bracket: the sub-bracket that produced it
  '''
  edges = np.linspace(a, b, n_sub + 1)
  best_x, best_bracket, best_d = None, None, np.inf
  for lo, hi in zip(edges[:-1], edges[1:]):
    x = quiet(golden_bisection, x0, y0, f, lo, hi)
    d = distance(x, x0, f(x), y0)
    if d < best_d:
      best_x, best_bracket, best_d = x, (lo, hi), d
  print(f'  golden best sub-bracket [{best_bracket[0]:.2f}, '
        f'{best_bracket[1]:.2f}] -> x {best_x:+.4f}, distance {best_d:.4f}')
  return best_x, best_bracket

def plot_comparison(x0, y0, f, naive_x, fixed_x, method='method5'):
  '''
  Left: the two candidate segments on the curve.
  Right: D(x) with every stationary point marked.
  '''
  d_naive = distance(naive_x, x0, f(naive_x), y0)
  d_fixed = distance(fixed_x, x0, f(fixed_x), y0)
  D = lambda x: (x - x0)**2 + (f(x) - y0)**2

  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

  xs = np.linspace(-4, 4, 400)
  ax1.plot(xs, f(xs), color='#2a78d6', linewidth=2, label='f(x)')
  ax1.plot([x0, naive_x], [y0, f(naive_x)], color='#eb6834', linewidth=2,
           linestyle='--', marker='o', markersize=8,
           label=f'local minimum, d = {d_naive:.3f}')
  ax1.plot([x0, fixed_x], [y0, f(fixed_x)], color='#1baf7a', linewidth=2,
           marker='o', markersize=8,
           label=f'global minimum, d = {d_fixed:.3f}')
  ax1.plot(x0, y0, 'o', color='#1a1a19', markersize=9, zorder=5,
           label=f'query point ({x0}, {y0})')
  ax1.set_xlim(-4.5, 4.5)
  ax1.set_ylim(4, 18)
  ax1.grid(True, color='#d8d8d4', linewidth=0.6)
  ax1.set_axisbelow(True)
  ax1.set_xlabel('x')
  ax1.set_ylabel('y')
  ax1.set_title(f'Both normals from ({x0}, {y0})')
  ax1.legend(loc='upper left', framealpha=0.9, fontsize=8)

  xd = np.linspace(-4, 4, 400)
  ax2.plot(xd, D(xd), color='#2a78d6', linewidth=2, label='D(x)')
  for root in np.sort(np.roots([4, 0, -18, -4])).real:
    ax2.plot(root, D(root), 'o', color='#52514e', markersize=8, zorder=3)
    ax2.annotate(f'{root:.3f}', (root, D(root)), textcoords='offset points',
                 xytext=(0, 14), ha='center', color='#52514e', fontsize=9)
  ax2.plot(naive_x, D(naive_x), 'o', color='#eb6834', markersize=10, zorder=4)
  ax2.plot(fixed_x, D(fixed_x), 'o', color='#1baf7a', markersize=10, zorder=4)
  ax2.grid(True, color='#d8d8d4', linewidth=0.6)
  ax2.set_axisbelow(True)
  ax2.set_xlabel('x')
  ax2.set_ylabel('D(x)')
  ax2.set_title("D(x) has two local minima (stationary points of D'(x))")
  ax2.legend(loc='upper center', framealpha=0.9)

  fig.tight_layout()
  out_dir = Path(__file__).parent / method
  out_dir.mkdir(exist_ok=True)
  out = out_dir / f'fig_comparison_point_{x0:.3f}_{y0:.3f}.png'
  fig.savefig(out, dpi=150, bbox_inches='tight')
  plt.close(fig)
  print(f'Saved {out}')

if __name__ == '__main__':
  x0, y0 = 2, 10

  print(f'Point ({x0}, {y0}) -- f({x0}) = {f(x0)}, so the point lies '
        f'inside the curve')
  print("Roots of D'(x) = 4x^3 - 18x - 4:",
        np.sort(np.roots([4, 0, -18, -4])).round(4))

  print('\nSingle start (the failure):')
  naive_x = quiet(newton_polynomial, x0, y0, f, df, ddf, 1.0)
  print(f'  newton guess  +1.00 -> x {naive_x:+.4f}, distance '
        f'{distance(naive_x, x0, f(naive_x), y0):.4f}')
  plot(naive_x, x0, f, y0, 'method5', 'newton_single_init_1.000')

  print('\nMulti-start Newton (the fix):')
  fixed_x, best_guess = multi_start_newton(x0, y0, f, df, ddf,
                                           (-5.0, -1.0, 1.0, 5.0))
  plot(fixed_x, x0, f, y0, 'method5', f'newton_multi_init_{best_guess:.3f}')

  print('\nMulti-bracket golden-section (the fix):')
  golden_x, best_bracket = multi_bracket_golden(x0, y0, f, -10, 10, 8)
  plot(golden_x, x0, f, y0, 'method5', 'golden_multi_bracket')

  xs = np.linspace(-10, 10, 2_000_001)
  d = np.hypot(xs - x0, f(xs) - y0)
  print(f'\nBrute-force reference: x = {xs[d.argmin()]:+.4f}, '
        f'distance = {d.min():.4f}')

  plot_comparison(x0, y0, f, naive_x, fixed_x)

  # the Newton construction for each guess: the tangent walks to whichever
  # root of D'(x) it is nearest, which is what decides the outcome
  for guess in (1.0, 5.0):
    plot_newton_steps(x0, y0, f, df, ddf, guess, 5, method='method5',
                      span=1.5)

  # the golden-section bracket over the interval that contains all three
  # stationary points
  plot_golden_intervals(x0, y0, f, -10, 10, 8, method='method5')

  # the intermediate-step figures used in the Discussion, for (-8, 0)
  plot_newton_steps(-8, 0, f, df, ddf, 3.0, 4, method='method1', span=1.5)
  plot_golden_intervals(-8, 0, f, -10, 10, 8, method='method2')

  # two further points inside the curve, solved with the multi-start fix
  for x0, y0 in ((3, 16), (-4, 25)):
    print(f'\nPoint ({x0}, {y0}):')
    fixed_x, best_guess = multi_start_newton(x0, y0, f, df, ddf,
                                             (-5.0, -1.0, 1.0, 5.0))
    print(f'  best: x {fixed_x:+.4f}, distance '
          f'{distance(fixed_x, x0, f(fixed_x), y0):.4f}')
    plot(fixed_x, x0, f, y0, 'method5', f'multi_init_{best_guess:.3f}')

  # the same multi-start scheme applied to non-polynomial curves
  others = (
    ('exponential', np.exp, np.exp, np.exp,
     (-4., 2.), (1., 0.), (-3., -1., 0., 1.)),
    ('logarithm', np.log, lambda x: 1/x, lambda x: -1/x**2,
     (0.05, 6.), (1., 3.), (0.5, 1., 2., 4.)),
    ('square root', np.sqrt, lambda x: 1/(2*np.sqrt(x)),
     lambda x: -1/(4*x**1.5), (0.01, 8.), (5., 0.), (0.5, 2., 4., 6.)),
  )
  for label, g, dg, ddg, domain, (px, py), guesses in others:
    print(f'\n{label}, point ({px}, {py}), domain {domain}:')
    best_x, _ = multi_start_newton(px, py, g, dg, ddg, guesses, domain)
    xs = np.linspace(domain[0], domain[1], 2_000_001)
    d = np.hypot(xs - px, g(xs) - py)
    print(f'  best:  x {best_x:+.4f}, distance '
          f'{distance(best_x, px, g(best_x), py):.4f}')
    print(f'  brute: x {xs[d.argmin()]:+.4f}, distance {d.min():.4f}')
    plot_curve(px, py, g, best_x, domain, label)
    plot_iterates(px, py, g, newton_iterates(px, py, g, dg, ddg, guesses[-1], 4),
                  domain, label)
