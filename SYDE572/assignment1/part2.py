import numpy as np

from part1 import plot

def golden_bisection(x0, y0, f, a, b, tolerance=1e-7):
  phi = (1 + np.sqrt(5))/2
  resphi = 2 - phi
  x1 = update_x1(a, b, resphi)
  x2 = update_x2(a, b, resphi)
  dist_x1 = objective_fn(x1, x0, f(x1), y0)
  dist_x2 = objective_fn(x2, x0, f(x2), y0)
  i = 0
  print(f'{"epoch":>5} {"a":>10} {"b":>10} {"x1":>10} {"x2":>10} '
        f'{"D(x1)":>12} {"D(x2)":>12}')
  while abs(b-a) > tolerance:
    i += 1
    if dist_x1 < dist_x2:
      b = x2
      x2 = x1
      dist_x2 = dist_x1
      x1 = update_x1(a, b, resphi)
      dist_x1 = objective_fn(x1, x0, f(x1), y0)
    else:
      a = x1
      x1 = x2
      dist_x1 = dist_x2
      x2 = update_x2(a, b, resphi)
      dist_x2 = objective_fn(x2, x0, f(x2), y0)
    print(f'{i:>5d} {a:>10.4f} {b:>10.4f} {x1:>10.4f} {x2:>10.4f} '
          f'{dist_x1:>12.4f} {dist_x2:>12.4f}')
  return (a+b)/2

def objective_fn(x, x0, f, y0):
  return (x-x0)**2+(f-y0)**2

def distance(x, x0, f, y0):
  return np.sqrt((x-x0)**2+(f-y0)**2)

def update_x1(a, b, resphi):
  return a + resphi * (b-a)

def update_x2(a, b, resphi):
  return b - resphi * (b-a)

f = lambda x: x**2+5

points = ((0, 0), (-4, 0), (-8, 0), (2, 0), (6, 0))
brackets = ((-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10))

for (x0, y0), (a, b) in zip(points, brackets):
  print(f'\n\n Points: ({x0}, {y0}), Bracket: [{a}, {b}]')
  best_x = golden_bisection(x0=x0, y0=y0, f=f, a=a, b=b)
  print(f'Summary: Best x: {best_x:.4f}, '
        f'Distance: {distance(best_x, x0, f(best_x), y0):.4f}')
  plot(best_x, x0, f, y0, 'method2', f'bracket_{a:.1f}_{b:.1f}')
