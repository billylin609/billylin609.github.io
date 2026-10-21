from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler

from dataLoader import DataLoader
from models.gaussian_basis import GaussianBasis
from models.polynomial_basis import PolynomialBasis

DATA_URL = 'http://lib.stat.cmu.edu/datasets/boston'
# Columns definition provided in the dataset file
COLUMNS = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS",
           "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]
N_TRAIN = 100
FIG_DIR = Path(__file__).resolve().parent / "figs"


def plot_rms(degrees, train_rms, test_rms, out_path: Path):
    x = np.arange(len(degrees))
    width = 0.36
    gap = 0.02  # small surface gap between the paired bars

    fig, ax = plt.subplots(figsize=(8, 4.8))
    groups = [(train_rms, "Training", "#2a78d6", -1), (test_rms, "Test", "#eb6834", 1)]
    for values, label, color, side in groups:
        bars = ax.bar(x + side * (width + gap) / 2, values, width, label=label,
                      color=color, zorder=2)
        # value at the tip of each bar, in text color (not the series color)
        ax.bar_label(bars, labels=[f"{v:.2g}" for v in values], padding=2,
                     fontsize=8, color="#3d3d3a")

    # log scale: test error spans ~1e1 to ~1e16; bars start from a fixed baseline below the smallest value
    ax.set_yscale("log")
    ax.set_ylim(bottom=0.5, top=max(test_rms) * 20)
    ax.set_xticks(x, [str(d) for d in degrees])
    ax.set_xlabel("Polynomial degree")
    ax.set_ylabel("RMS error ($1000s, log scale)")
    ax.set_title("Polynomial basis regression: RMS error vs. degree")
    ax.grid(True, axis="y", which="major", color="#e4e3df", linewidth=0.8, zorder=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(frameon=False, loc="upper left")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    return fig


def plot_poly1d(x_train, y_train, x_test, y_test, grid, curve, degree, name,
                train_rms, test_rms, out_path: Path):
    '''
    One figure per degree for Part 1c: the learned polynomial against the
    training split on the left and the same curve against the test split on the
    right. Both panels share axes so the two can be compared directly.
    '''
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), sharex=True, sharey=True)

    panels = [(axes[0], x_train, y_train, "Training", "#2a78d6", True, train_rms),
              (axes[1], x_test, y_test, "Test", "#eb6834", False, test_rms)]
    for ax, x, y, label, color, filled, rms in panels:
        ax.plot(grid, curve, color="#3d3d3a", linewidth=2,
                label=f"Degree {degree} fit", zorder=4)
        if filled:
            ax.scatter(x, y, s=30, color=color, label=f"{label} data", zorder=3)
        else:
            ax.scatter(x, y, s=30, marker="^", linewidths=1.2, facecolors="none",
                       edgecolors=color, label=f"{label} data", zorder=3)

        # RMS blows up past a few thousand at high degree; switch to scientific there
        rms_label = f"{rms:,.3f}" if rms < 1e4 else f"{rms:.3e}"
        ax.set_title(f"{label} set — RMS = {rms_label}", fontsize=11)
        ax.set_xlabel(f"{name} (normalized)")
        ax.grid(True, color="#e4e3df", linewidth=0.8, zorder=0)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        ax.legend(frameon=False, loc="upper left", fontsize=9)

    # open the view far enough to show where the high-order curves start to
    # diverge, but cap it at 1.5x the data span so the points stay readable.
    # Prices are positive, so the view starts at 0 however far a curve dives,
    # and 25% of headroom is left at the top as a clear band for the legend.
    y_all = np.concatenate([y_train, y_test])
    lo, hi = y_all.min(), y_all.max()
    pad, cap = 0.1 * (hi - lo), 1.5 * (hi - lo)
    top = max(hi + pad, min(curve.max(), hi + cap))
    axes[0].set_ylim(0, top * 1.25)
    axes[0].set_ylabel("MEDV ($1000s)")

    fig.suptitle(f"{name}: degree {degree} polynomial fit")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_gaussian_overlap(centers, a_values, out_path: Path, ncols=2):
    '''
    The same basis drawn at each width a: one panel per value, wide bumps that
    overlap and cover the axis through to narrow bumps that leave gaps between
    the centres. The dashed line is the sum of the bumps, i.e. how much basis
    there is to fit with at each x. Panels share a y axis so the sums compare.
    '''
    x = np.linspace(centers.min() - 0.7, centers.max() + 0.7, 600)
    spacing = float(np.mean(np.diff(centers)))
    shades = ["#9ec5e8", "#6ba4d9", "#2a78d6", "#1b4f8c", "#0d2a4d"]

    nrows = int(np.ceil(len(a_values) / ncols))
    fig, axes = plt.subplots(nrows, ncols, figsize=(5.6 * ncols, 3.9 * nrows),
                             sharex=True, sharey=True, squeeze=False)
    flat = axes.ravel()
    for ax, a in zip(flat, a_values):
        bumps = np.exp(a * (x[:, None] - centers[None, :]) ** 2)
        for k in range(len(centers)):
            ax.plot(x, bumps[:, k], linewidth=1.8, color=shades[k % len(shades)])
        ax.plot(x, bumps.sum(axis=1), linewidth=2, linestyle="--", color="#eb6834",
                label="sum of all bumps")
        ax.scatter(centers, np.zeros(len(centers)), s=45, color="#3d3d3a",
                   zorder=5, label="centres $c_k$")

        # value a neighbouring bump still has at the midpoint between centres
        midpoint = np.exp(a * (spacing / 2) ** 2)
        ax.set_title(f"$a$ = {a:g}:  $\\phi$ = {midpoint:.3f} midway between centres")
        ax.grid(True, color="#e4e3df", linewidth=0.8)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        ax.legend(frameon=False, fontsize=9, loc="upper right")

    for ax in flat[len(a_values):]:
        ax.set_visible(False)
    for ax in axes[-1]:
        ax.set_xlabel("$x$")
    for ax in axes[:, 0]:
        ax.set_ylabel(r"$\phi_k(x)$")

    flat[0].set_ylim(-0.1, None)
    fig.suptitle("Gaussian basis coverage at each width")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_gaussian_shape(a_values, median_distance, out_path: Path):
    '''
    The basis function phi(r) = exp(a * r^2) against the distance r from its
    centre, for a range of a. The dashed line marks the median distance between
    the normalized training points, which is the spacing the bumps have to span.
    '''
    r = np.linspace(0, 1.6, 400)
    # light to dark as the bumps get narrower
    shades = ["#c6dbf0", "#9ec5e8", "#6ba4d9", "#2a78d6", "#1b4f8c", "#0d2a4d"]

    fig, ax = plt.subplots(figsize=(7, 4.6))
    for a, color in zip(a_values, shades):
        ax.plot(r, np.exp(a * r ** 2), linewidth=2, color=color, label=f"$a$ = {a:g}")
    ax.axvline(median_distance, color="#eb6834", linestyle="--", linewidth=1.6,
               label=f"median centre spacing ({median_distance:.2f})")

    ax.set_xlim(0, 1.6)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel(r"Distance from centre $\|x - c_k\|$")
    ax.set_ylabel(r"$\phi_k(x)$")
    ax.set_title(r"Gaussian basis function shape for a range of $a$")
    ax.grid(True, color="#e4e3df", linewidth=0.8)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(frameon=False, fontsize=9)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_gaussian_rms(n_basis, series, split, out_path: Path):
    '''
    Part 2e: RMS against the number of Gaussian basis functions as grouped bars,
    one bar per width a within each K. series maps a -> the RMS values lined up
    with n_basis.
    '''
    # light to dark as the bumps get narrower
    shades = ["#9ec5e8", "#4a90d9", "#1b4f8c", "#0d2a4d"]
    x = np.arange(len(n_basis))
    width = 0.8 / len(series)

    fig, ax = plt.subplots(figsize=(10, 4.8))
    for i, ((a, values), color) in enumerate(zip(series.items(), shades)):
        offset = (i - (len(series) - 1) / 2) * width
        ax.bar(x + offset, values, width * 0.9, color=color,
               label=f"$a$ = {a:g}", zorder=2)

    # log scale: the test bars span one value to several hundred
    flat = [v for values in series.values() for v in values]
    ax.set_yscale("log")
    ax.set_ylim(min(flat) / 2, max(flat) * 4)
    ax.set_xticks(x, [str(k) for k in n_basis])
    ax.set_xlabel("Number of basis functions $K$")
    ax.set_ylabel(f"{split} RMS error ($1000s, log scale)")
    ax.set_title(f"Gaussian basis regression: {split.lower()} error vs. $K$")
    ax.grid(True, axis="y", which="major", color="#e4e3df", linewidth=0.8, zorder=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(frameon=False, fontsize=9, ncol=4, loc="upper left")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_lambda_series(lams, series, out_path: Path, ylabel, title,
                       marks, mark_label):
    '''
    Part 2f: RMS against the regularizing constant on a log axis, one line per
    width a. lambda = 0 has no position on a log axis and is left out of lams.
    marks maps a -> the index to ring on that line.
    '''
    # light to dark as the bumps get narrower
    shades = ["#9ec5e8", "#4a90d9", "#1b4f8c", "#0d2a4d"]
    markers = ["o", "s", "^", "D"]

    fig, ax = plt.subplots(figsize=(7.5, 4.8))
    for (a, values), color, marker in zip(series.items(), shades, markers):
        ax.semilogx(lams, values, marker=marker, linewidth=2, color=color,
                    label=f"$a$ = {a:g}", zorder=3)
        i = marks[a]
        ax.scatter([lams[i]], [values[i]], s=110, facecolors="none",
                   edgecolors="#eb6834", linewidths=1.8, zorder=4)

    ax.set_yscale("log")
    ax.set_xlabel(r"Regularizing constant $\lambda$ (log scale)")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, which="both", color="#e4e3df", linewidth=0.8, zorder=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(frameon=False, fontsize=9, title=mark_label, title_fontsize=8)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_cv_lambda(lams, val_rms, out_path: Path, title, log_scale=True,
                   label="Mean validation RMS"):
    '''
    Part 1d: an RMS series (by default the average 10-fold validation RMS)
    against the regularizing constant, on a semilogx axis, or a linear one with
    log_scale=False. lams and val_rms exclude lambda = 0, which has no position
    on a log axis.
    '''
    best = int(np.argmin(val_rms))

    fig, ax = plt.subplots(figsize=(7, 4.6))
    plot = ax.semilogx if log_scale else ax.plot
    plot(lams, val_rms, marker="o", linewidth=2, color="#2a78d6",
         label=label, zorder=3)
    ax.scatter([lams[best]], [val_rms[best]], s=110, facecolors="none",
               edgecolors="#3d3d3a", linewidths=1.8, zorder=4,
               label=f"Lowest: $\\lambda$ = {lams[best]:g} ({val_rms[best]:.3f})")

    ax.set_xlabel("Regularizing constant $\\lambda$" + (" (log scale)" if log_scale else ""))
    ax.set_ylabel("RMS error ($1000s)")
    ax.set_title(title)
    ax.grid(True, which="both", color="#e4e3df", linewidth=0.8, zorder=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(frameon=False, fontsize=9)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_ridge_fits(x, y, grid, fits, degree, name, split, out_path: Path, y_top):
    '''
    Part 1d: one panel per lambda, each with one split's points and that
    lambda's degree-`degree` ridge curve. fits maps lambda -> (curve, rms on this
    split); split is "Training" or "Test". y_top is shared by the train and test
    figures so the two can be compared directly.
    '''
    color, filled = ("#2a78d6", True) if split == "Training" else ("#eb6834", False)
    n_cols = 3
    n_rows = int(np.ceil(len(fits) / n_cols))
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(13, 4 * n_rows),
                             sharex=True, sharey=True)
    axes = np.atleast_1d(axes).ravel()

    for ax, (lam, (curve, rms)) in zip(axes, fits.items()):
        if filled:
            ax.scatter(x, y, s=18, color=color, label=f"{split} data", zorder=3)
        else:
            ax.scatter(x, y, s=18, marker="^", linewidths=1, facecolors="none",
                       edgecolors=color, label=f"{split} data", zorder=3)
        ax.plot(grid, curve, color="#3d3d3a", linewidth=2, label="Ridge fit", zorder=4)
        ax.set_title(f"$\\lambda$ = {lam:g} — RMS = {rms:,.2f}", fontsize=10)
        ax.grid(True, color="#e4e3df", linewidth=0.8, zorder=0)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
    for ax in axes[len(fits):]:
        ax.set_visible(False)
    for ax in axes[-n_cols:]:
        ax.set_xlabel(f"{name} (normalized)")
    for ax in axes[::n_cols]:
        ax.set_ylabel("MEDV ($1000s)")

    # prices start at 0; curves that dive or shoot off are cut by y_top
    axes[0].set_ylim(0, y_top)
    axes[0].legend(frameon=False, loc="upper right", fontsize=8)

    fig.suptitle(f"{name}: degree {degree} ridge fit on the {split.lower()} set for each $\\lambda$")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    loader = DataLoader(DATA_URL, COLUMNS)
    X_all = loader.drop("MEDV")
    loader.train_test_split(X_all, loader["MEDV"], N_TRAIN, False)
    X_train, y_train = loader.get_train()
    X_test, y_test = loader.get_test()

    degrees = list(range(1, 8))
    train_rms, test_rms = [], []
    for degree in degrees:
        model = PolynomialBasis(degree).fit(X_train, y_train)
        train_rms.append(model.evaluate(X_train, y_train))
        test_rms.append(model.evaluate(X_test, y_test))
        print(f"degree {degree}: train RMS = {train_rms[-1]:.4f}, "
              f"test RMS = {test_rms[-1]:.4e}")

    FIG_DIR.mkdir(exist_ok=True)
    out_path = FIG_DIR / "polynomial_rms.png"
    plot_rms(degrees, train_rms, test_rms, out_path)
    print(f"plot saved to {out_path}")

    print()

    scaler = MinMaxScaler().fit(X_all)
    X_train_norm, X_test_norm = scaler.transform(X_train), scaler.transform(X_test)

    raw_model = PolynomialBasis(degree=1).fit(X_train, y_train)
    model = PolynomialBasis(degree=1).fit(X_train_norm, y_train)
    raw_bias, raw_w = raw_model.w[0], raw_model.w[1:]
    bias, w = model.w[0], model.w[1:]

    print(f"{'':<10}{'raw':>12}{'normalized':>12}")
    print(f"{'bias':<10}{raw_bias:>12.4f}{bias:>12.4f}")
    for name, rw, nw in zip(COLUMNS[:-1], raw_w, w):
        print(f"{name:<10}{rw:>12.4f}{nw:>12.4f}")

    print()

    print(f"{'':<12}{'train RMS':>12}{'test RMS':>12}")
    for label, m, A, B in (("raw", raw_model, X_train, X_test),
                           ("normalized", model, X_train_norm, X_test_norm)):
        print(f"{label:<12}{m.evaluate(A, y_train):>12.4f}{m.evaluate(B, y_test):>12.4f}")

    print()

    feature = 2
    name = COLUMNS[feature]
    x_train, x_test = X_train[:, [feature]], X_test[:, [feature]]

    scaler_1d = MinMaxScaler().fit(X_all[:, [feature]])
    x_train_norm = scaler_1d.transform(x_train)
    x_test_norm = scaler_1d.transform(x_test)

    grid = np.linspace(min(x_train_norm.min(), x_test_norm.min()),
                       max(x_train_norm.max(), x_test_norm.max()), 400).reshape(-1, 1)

    print(f"single-feature fits on {name} (column {feature}, 0-based)")
    print(f"{'degree':<8}{'train RMS':>12}{'test RMS':>14}")
    for degree in degrees:
        model = PolynomialBasis(degree).fit(x_train_norm, y_train)
        train_rms_1d = model.evaluate(x_train_norm, y_train)
        test_rms_1d = model.evaluate(x_test_norm, y_test)
        print(f"{degree:<8}{train_rms_1d:>12.4f}{test_rms_1d:>14.4e}")

        out_path = FIG_DIR / f"poly1d_{name.lower()}_degree{degree}.png"
        plot_poly1d(x_train_norm, y_train, x_test_norm, y_test, grid,
                    model.predict(grid), degree, name,
                    train_rms_1d, test_rms_1d, out_path)
    print(f"figures saved to {FIG_DIR}/poly1d_{name.lower()}_degree*.png")

    print()

    reg_degree = 8
    lambdas = [0.0, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
    n_weights = 1 + reg_degree  # single feature, so 1 + 1 * degree
    folds = KFold(n_splits=10, shuffle=True, random_state=0)

    reg_scaler = MinMaxScaler().fit(x_train)
    x_reg, x_reg_test = reg_scaler.transform(x_train), reg_scaler.transform(x_test)
    reg_grid = np.linspace(min(x_reg.min(), x_reg_test.min()),
                           max(x_reg.max(), x_reg_test.max()), 400).reshape(-1, 1)

    print(f"10-fold CV for a degree {reg_degree} fit on {name}")
    print(f"{'lambda':>10}{'mean val RMS':>16}{'mean train RMS':>18}"
          f"{'train RMS':>12}{'test RMS':>12}")
    mean_val, mean_train, reg_test_rms = [], [], []
    train_fits, test_fits = {}, {}
    for lam in lambdas:
        model = PolynomialBasis(reg_degree).regularized_fit(
            x_reg, y_train, np.full(n_weights, lam), cross_validation=True, folds=folds)
        mean_train.append(model.cv_train_rms)
        mean_val.append(model.cv_val_rms)

        fit_train = model.evaluate(x_reg, y_train)
        fit_test = model.evaluate(x_reg_test, y_test)
        print(f"{lam:>10g}{mean_val[-1]:>16.4f}{mean_train[-1]:>18.4f}"
              f"{fit_train:>12.4f}{fit_test:>12.4f}")

        if lam == 0.0:
            continue
        curve = model.predict(reg_grid)
        train_fits[lam] = (curve, fit_train)
        test_fits[lam] = (curve, fit_test)
        reg_test_rms.append(fit_test)

    best = int(np.argmin(mean_val))
    print(f"\nbest lambda = {lambdas[best]:g} (mean validation RMS {mean_val[best]:.4f})")
    print(f"unregularized baseline (lambda = 0): {mean_val[0]:.4f}")

    for log_scale, suffix in ((False, "_linear"), (True, "")):
        out_path = FIG_DIR / f"ridge_cv_lambda{suffix}.png"
        plot_cv_lambda(lambdas[1:], mean_val[1:], out_path,
                       f"Degree {reg_degree} polynomial: 10-fold CV error vs. $\\lambda$",
                       log_scale=log_scale)
        print(f"plot saved to {out_path}")

    out_path = FIG_DIR / "ridge_test_rms.png"
    plot_cv_lambda(lambdas[1:], reg_test_rms, out_path,
                   f"Degree {reg_degree} polynomial: test error vs. $\\lambda$",
                   label="Test RMS")
    print(f"plot saved to {out_path}")

    y_all = np.concatenate([y_train, y_test])
    y_top = (y_all.max() + 0.1 * np.ptp(y_all)) * 1.25
    for split, x_s, y_s, fits in (("Training", x_reg, y_train, train_fits),
                                  ("Test", x_reg_test, y_test, test_fits)):
        out_path = FIG_DIR / f"ridge_fit_{'train' if split == 'Training' else 'test'}.png"
        plot_ridge_fits(x_s, y_s, reg_grid, fits, reg_degree, name, split, out_path, y_top)
        print(f"plot saved to {out_path}")

    print()

    n_basis = list(range(5, 96, 10))
    a_values = [-0.1, -1.0, -5.0, -20.0]

    pair_dist = np.linalg.norm(X_train_norm[:, None, :] - X_train_norm[None, :, :], axis=-1)
    median_spacing = np.median(pair_dist[~np.eye(N_TRAIN, dtype=bool)])
    out_path = FIG_DIR / "gaussian_shape.png"
    plot_gaussian_shape([-0.1, -0.5, -1, -2, -5, -20], median_spacing, out_path)
    print(f"plot saved to {out_path}")

    out_path = FIG_DIR / "gaussian_overlap.png"
    plot_gaussian_overlap(np.arange(5) * median_spacing, a_values, out_path)
    print(f"plot saved to {out_path}")
    print()

    gauss_train = {a: [] for a in a_values}
    gauss_test = {a: [] for a in a_values}
    for k in n_basis:
        for a in a_values:
            model = GaussianBasis(X_train_norm, n_centers=k, a=a).fit(X_train_norm, y_train)
            gauss_train[a].append(model.evaluate(X_train_norm, y_train))
            gauss_test[a].append(model.evaluate(X_test_norm, y_test))

    header = "".join(f"{f'a={a:g}':>14}" for a in a_values)
    for split, series in (("train", gauss_train), ("test", gauss_test)):
        print(f"{split} RMS")
        print(f"{'K':<6}{header}")
        for i, k in enumerate(n_basis):
            print(f"{k:<6}" + "".join(f"{series[a][i]:>14.4f}" for a in a_values))
        print()

    for split, series in (("Training", gauss_train), ("Test", gauss_test)):
        out_path = FIG_DIR / f"gaussian_rms_{split.lower()}.png"
        plot_gaussian_rms(n_basis, series, split, out_path)
        print(f"plot saved to {out_path}")

    print()

    n_centers_g = 90
    n_weights_g = 1 + n_centers_g

    cv_val_g = {a: [] for a in a_values}
    test_g = {a: [] for a in a_values}
    for a in a_values:
        for lam in lambdas:
            model = GaussianBasis(X_train_norm, n_centers=n_centers_g, a=a).regularized_fit(
                X_train_norm, y_train, np.full(n_weights_g, lam),
                cross_validation=True, folds=folds)
            cv_val_g[a].append(model.cv_val_rms)
            test_g[a].append(model.evaluate(X_test_norm, y_test))

    header = "".join(f"{f'a={a:g}':>14}" for a in a_values)
    print(f"{n_centers_g} centre Gaussian basis, all {X_train_norm.shape[1]} features")
    for split, series in (("mean 10-fold validation RMS", cv_val_g),
                          ("test RMS", test_g)):
        print(f"{split}")
        print(f"{'lambda':<8}{header}")
        for i, lam in enumerate(lambdas):
            print(f"{lam:<8g}" + "".join(f"{series[a][i]:>14.4f}" for a in a_values))
        print()

    for a in a_values:
        best_g = int(np.argmin(cv_val_g[a]))
        print(f"a={a:>6g}: best lambda = {lambdas[best_g]:<7g} "
              f"(validation RMS {cv_val_g[a][best_g]:8.4f}, "
              f"test RMS {test_g[a][best_g]:8.4f})")

    cv_choice = {a: int(np.argmin(cv_val_g[a][1:])) for a in a_values}
    plots = ((cv_val_g, "gaussian_cv_lambda.png", "Mean validation RMS ($1000s)",
              f"{n_centers_g} Gaussian basis functions: 10-fold CV error"),
             (test_g, "gaussian_test_lambda.png", "Test RMS ($1000s)",
              f"{n_centers_g} Gaussian basis functions: test error"))
    for series, filename, ylabel, title in plots:
        out_path = FIG_DIR / filename
        plot_lambda_series(lambdas[1:], {a: v[1:] for a, v in series.items()},
                           out_path, ylabel, title + r" vs. $\lambda$",
                           cv_choice, r"orange ring = $\lambda$ chosen by CV")
        print(f"plot saved to {out_path}")

    plt.show()
