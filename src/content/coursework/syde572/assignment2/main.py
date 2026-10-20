from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

from dataLoader import DataLoader
from models.polynomial_basis import PolynomialBasis

DATA_URL = 'http://lib.stat.cmu.edu/datasets/boston'
# Columns definition provided in the dataset file
COLUMNS = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS",
           "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]
N_TRAIN = 100
FIG_DIR = Path(__file__).resolve().parent / "figs"


def polynomial_regression(X_train, y_train, X_test, y_test, degrees):
    '''
    Part 1a: fit an unregularized polynomial basis regression for each degree.
    Returns the training and test RMS error per degree.
    '''
    train_rms, test_rms = [], []
    for degree in degrees:
        model = PolynomialBasis(degree).fit(X_train, y_train)
        train_rms.append(model.evaluate(X_train, y_train))
        test_rms.append(model.evaluate(X_test, y_test))
    return train_rms, test_rms


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


def part1a(X_train, y_train, X_test, y_test):
    degrees = list(range(1, 8))
    train_rms, test_rms = polynomial_regression(X_train, y_train, X_test, y_test, degrees)
    for d, tr, te in zip(degrees, train_rms, test_rms):
        print(f"degree {d}: train RMS = {tr:.4f}, test RMS = {te:.4e}")

    FIG_DIR.mkdir(exist_ok=True)
    out_path = FIG_DIR / "polynomial_rms.png"
    plot_rms(degrees, train_rms, test_rms, out_path)
    print(f"plot saved to {out_path}")


def part1b(X_train, y_train, scaler: StandardScaler):
    '''
    Part 1b: degree 1 fit, report the learned weights.
    The model is trained on standardized features z = (x - mu) / sigma, so each weight is
    "$1000s per training standard deviation". Undo the normalization to get per-unit weights:
        y = b + sum_j w_j z_j  =>  w_j' = w_j / sigma_j,  b' = b - sum_j w_j * mu_j / sigma_j
    '''
    model = PolynomialBasis(degree=1).fit(X_train, y_train)
    bias, w = model.w[0], model.w[1:]
    mu, sigma = scaler.mean_, scaler.scale_
    w_orig = w / sigma
    bias_orig = bias - np.sum(w * mu / sigma)

    features = COLUMNS[:-1]
    print(f"{'weight':<8}{'feature':<10}{'standardized':>14}{'original units':>16}")
    print(f"{'bias':<8}{'':<10}{bias:>14.4f}{bias_orig:>16.4f}")
    for j, name in enumerate(features):
        print(f"{'w' + str(j):<8}{name:<10}{w[j]:>14.4f}{w_orig[j]:>16.4f}")

    rm, dis = features.index("RM"), features.index("DIS")
    print(f"\nRM  (6th feature, w{rm}): {w[rm]:.4f} per std ({sigma[rm]:.3f} rooms) "
          f"= {w_orig[rm]:.4f} ($1000s per room)")
    print(f"DIS (8th feature, w{dis}): {w[dis]:.4f} per std ({sigma[dis]:.3f}) "
          f"= {w_orig[dis]:.4f} ($1000s per unit of weighted distance)")


def compare_standardization(X_train, y_train, X_test, y_test, scaler: StandardScaler):
    '''
    Run the Part 1a sweep on raw and on standardized features and compare the RMS errors.
    X_train / X_test are the raw (unscaled) features.
    '''
    degrees = list(range(1, 8))
    raw_train, raw_test = polynomial_regression(X_train, y_train, X_test, y_test, degrees)
    std_train, std_test = polynomial_regression(
        scaler.transform(X_train), y_train, scaler.transform(X_test), y_test, degrees)

    print(f"{'degree':<8}{'train raw':>12}{'train std':>12}{'test raw':>14}{'test std':>14}")
    for d, rtr, str_, rte, ste in zip(degrees, raw_train, std_train, raw_test, std_test):
        print(f"{d:<8}{rtr:>12.4f}{str_:>12.4f}{rte:>14.4e}{ste:>14.4e}")

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    # training error spans ~0.9-3.8 (linear); test error spans ~1e1-1e16 (log)
    panels = [(axes[0], raw_train, std_train, "Training RMS error", "linear"),
              (axes[1], raw_test, std_test, "Test RMS error (log scale)", "log")]
    for ax, raw, std, title, scale in panels:
        ax.plot(degrees, raw, marker="o", linewidth=2, color="#2a78d6", label="Raw features")
        ax.plot(degrees, std, marker="s", linewidth=2, color="#eb6834", label="Standardized")
        ax.set_yscale(scale)
        ax.set_title(title)
        ax.set_xlabel("Polynomial degree")
        ax.set_xticks(degrees)
        ax.grid(True, axis="y", which="major", color="#e4e3df", linewidth=0.8)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
    axes[0].set_ylabel("RMS error ($1000s)")
    axes[0].legend(frameon=False)
    fig.tight_layout()

    FIG_DIR.mkdir(exist_ok=True)
    out_path = FIG_DIR / "standardization_rms.png"
    fig.savefig(out_path, dpi=150)
    print(f"plot saved to {out_path}")


if __name__ == "__main__":
    loader = DataLoader(DATA_URL, COLUMNS)
    # first 100 points for training, the remainder for testing
    loader.train_test_split(loader.drop("MEDV"), loader["MEDV"], N_TRAIN, False)
    X_train, y_train = loader.get_train()
    X_test, y_test = loader.get_test()

    # standardize with training statistics so high powers (e.g. TAX^7 ~ 1e19)
    # don't make the design matrix ill-conditioned; StandardScaler leaves
    # zero-variance columns (CHAS is all 0 in the first 100 rows) unscaled
    scaler = StandardScaler().fit(X_train)
    X_train_std, X_test_std = scaler.transform(X_train), scaler.transform(X_test)

    part1a(X_train_std, y_train, X_test_std, y_test)
    print()
    part1b(X_train_std, y_train, scaler)
    print()
    compare_standardization(X_train, y_train, X_test, y_test, scaler)
    plt.show()
