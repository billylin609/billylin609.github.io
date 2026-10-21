from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import KFold
from sklearn.preprocessing import MinMaxScaler

from dataLoader import DataLoader
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


def plot_cv_lambda(lams, val_rms, baseline, out_path: Path):
    '''
    Part 1d: average 10-fold validation RMS against the regularizing constant.
    lams and val_rms exclude lambda = 0, which has no position on a log axis;
    it is drawn as a horizontal baseline instead.
    '''
    best = int(np.argmin(val_rms))

    fig, ax = plt.subplots(figsize=(7, 4.6))
    ax.semilogx(lams, val_rms, marker="o", linewidth=2, color="#2a78d6",
                label="Mean validation RMS", zorder=3)
    ax.axhline(baseline, color="#eb6834", linestyle="--", linewidth=1.8,
               label=f"Unregularized ($\\lambda = 0$): {baseline:,.3f}", zorder=2)
    ax.scatter([lams[best]], [val_rms[best]], s=110, facecolors="none",
               edgecolors="#3d3d3a", linewidths=1.8, zorder=4,
               label=f"Best $\\lambda$ = {lams[best]:g} ({val_rms[best]:.3f})")

    ax.set_xlabel("Regularizing constant $\\lambda$ (log scale)")
    ax.set_ylabel("RMS error ($1000s)")
    ax.set_title("10-fold cross-validation error vs. $\\lambda$")
    ax.grid(True, which="both", color="#e4e3df", linewidth=0.8, zorder=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.legend(frameon=False, fontsize=9)
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

    # L2-regularized degree 8 fit on the first 100 points, second feature only.
    # lambda = 0 is kept in the sweep as the unregularized baseline.
    reg_degree = 8
    lambdas = [0.0, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
    n_weights = 1 + reg_degree  # single feature, so 1 + 1 * degree
    folds = KFold(n_splits=10, shuffle=True, random_state=0)

    # This part uses the first 100 points as its whole dataset, so the scaler is
    # fitted on them rather than on all 506. Scaling them to [0, 1] instead of
    # [0, 0.53] keeps the basis columns O(1), which is the scale the lambda grid
    # above assumes.
    x_reg = MinMaxScaler().fit_transform(x_train)

    print(f"10-fold CV for a degree {reg_degree} fit on {name}")
    print(f"{'lambda':>10}{'mean val RMS':>16}{'mean train RMS':>18}")
    mean_val, mean_train = [], []
    for lam in lambdas:
        val_rms, train_rms_cv = [], []
        for train_idx, val_idx in folds.split(x_reg):
            model = PolynomialBasis(reg_degree).regularized_fit(
                x_reg[train_idx], y_train[train_idx], np.full(n_weights, lam))
            train_rms_cv.append(model.evaluate(x_reg[train_idx], y_train[train_idx]))
            val_rms.append(model.evaluate(x_reg[val_idx], y_train[val_idx]))
        mean_val.append(np.mean(val_rms))
        mean_train.append(np.mean(train_rms_cv))
        print(f"{lam:>10g}{mean_val[-1]:>16.4f}{mean_train[-1]:>18.4f}")

    best = int(np.argmin(mean_val))
    print(f"\nbest lambda = {lambdas[best]:g} (mean validation RMS {mean_val[best]:.4f})")
    print(f"unregularized baseline (lambda = 0): {mean_val[0]:.4f}")

    out_path = FIG_DIR / "ridge_cv_lambda.png"
    plot_cv_lambda(lambdas[1:], mean_val[1:], mean_val[0], out_path)
    print(f"plot saved to {out_path}")

    plt.show()
