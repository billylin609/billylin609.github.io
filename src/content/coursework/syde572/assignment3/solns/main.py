from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import Isomap

from dataLoader import DataLoader

DATA_URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
FEATURES = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]
TARGET = "species"
SPECIES = {"Iris-setosa": ("#2a78d6", "o"),
           "Iris-versicolor": ("#eb6834", "s"),
           "Iris-virginica": ("#1baf7a", "^")}
FIG_DIR = Path(__file__).resolve().parent.parent / "figs"


def save_figure(fig, axes, title, out_path: Path):
    '''Title the figure, add one legend shared by every panel, and save it.'''
    fig.suptitle(title)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.legend(*axes[0].get_legend_handles_labels(), frameon=False,
               ncol=len(SPECIES), loc="lower center")
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_histograms(X, y, out_path: Path):
    '''One feature at a time: a histogram per species on shared bins.'''
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    axes = axes.ravel()
    for feature, ax in enumerate(axes):
        bins = np.histogram_bin_edges(X[:, feature], bins=20)
        for species, (color, _) in SPECIES.items():
            ax.hist(X[y == species, feature], bins=bins, color=color, alpha=0.6,
                    label=species)
        ax.set(xlabel=FEATURES[feature], ylabel="Count")
    save_figure(fig, axes, "Iris marginalized onto one feature", out_path)


def plot_scatters(X, y, n_features, shape, out_path: Path):
    '''Scatter plot of every combination of 2 or 3 features.'''
    projection = "3d" if n_features == 3 else None
    fig, axes = plt.subplots(*shape, figsize=(12, 9), subplot_kw={"projection": projection})
    axes = axes.ravel()
    for dims, ax in zip(combinations(range(len(FEATURES)), n_features), axes):
        for species, (color, marker) in SPECIES.items():
            ax.scatter(*X[y == species][:, dims].T, s=25, color=color, marker=marker,
                       label=species)
        ax.set(**{f"{axis}label": FEATURES[d] for axis, d in zip("xyz", dims)})
        if n_features == 3:
            ax.view_init(elev=10, azim=-50)  # low camera keeps the gaps between clusters visible
    save_figure(fig, axes, f"Iris marginalized onto {n_features} features", out_path)


def plot_pca(Z, y, out_path: Path):
    '''The data marginalized onto the top 1, 2 and 3 principal components.'''
    fig = plt.figure(figsize=(15, 5.5))
    axes = [fig.add_subplot(1, 3, 1), fig.add_subplot(1, 3, 2),
            fig.add_subplot(1, 3, 3, projection="3d")]
    bins = np.histogram_bin_edges(Z[:, 0], bins=20)
    for species, (color, marker) in SPECIES.items():
        z = Z[y == species]
        axes[0].hist(z[:, 0], bins=bins, color=color, alpha=0.6, label=species)
        for ax, n_axes in zip(axes[1:], (2, 3)):
            ax.scatter(*z[:, :n_axes].T, s=25, color=color, marker=marker)
    axes[0].set(xlabel="PC1", ylabel="Count")
    axes[1].set(xlabel="PC1", ylabel="PC2")
    axes[2].set(xlabel="PC1", ylabel="PC2", zlabel="PC3")
    axes[2].set_box_aspect(None, zoom=0.85)  # leaves room for the PC3 label
    save_figure(fig, axes, "Iris marginalized onto the top principal components", out_path)


def plot_isomap(E, y, out_path: Path):
    '''Scatter plot of the 2-D Isomap embedding.'''
    fig, ax = plt.subplots(figsize=(7, 5.5))
    for species, (color, marker) in SPECIES.items():
        ax.scatter(*E[y == species].T, s=25, color=color, marker=marker, label=species)
    ax.set(xlabel="Component 1", ylabel="Component 2")
    save_figure(fig, [ax], "Iris reduced to two dimensions with Isomap (3 neighbours)", out_path)


if __name__ == "__main__":
    loader = DataLoader(DATA_URL, FEATURES + [TARGET])
    X, y = loader.drop(TARGET), loader[TARGET]

    FIG_DIR.mkdir(exist_ok=True)
    plot_histograms(X, y, FIG_DIR / "iris_one_feature.png")
    plot_scatters(X, y, 2, (2, 3), FIG_DIR / "iris_two_features.png")
    plot_scatters(X, y, 3, (2, 2), FIG_DIR / "iris_three_features.png")

    print(loader.df.groupby(TARGET).agg(["min", "max"]).T)

    pca = PCA(n_components=3).fit(X)
    Z = pca.transform(X)
    plot_pca(Z, y, FIG_DIR / "iris_pca.png")
    print(pca.components_.round(3))

    total = np.linalg.norm(X - X.mean(axis=0)) ** 2
    print(np.cumsum(np.sum(Z ** 2, axis=0)) / total)

    isomap = Isomap(n_neighbors=3, n_components=2)
    Z_isomap = isomap.fit_transform(X)
    plot_isomap(Z_isomap, y, FIG_DIR / "iris_isomap.png")

    # Isomap's total comes from geodesic distances, using the same formula as Part 4
    isomap_total = np.sum(isomap.dist_matrix_ ** 2) / (2 * len(X))
    print(f"PCA: {np.sum(Z[:, :2] ** 2) / total:.4f}")
    print(f"Isomap: {np.sum(Z_isomap ** 2) / isomap_total:.4f}")
