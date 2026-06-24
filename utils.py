import matplotlib.pyplot as plt
import numpy as np

def print_table(data:tuple):
    print(f"{'Iter':<5} | {'Raíz (xr)':<12} | {'Error (ea) %':<12}")
    for tuple in data:
        print(f"{tuple[0]:<5} | {tuple[1]:<12.6f} | {tuple[2]:<12.4f}")


def plot(func, points, x_markers=None, x_range=(-10, 10), num_samples=500, title=None):
    x = np.linspace(x_range[0], x_range[1], num_samples)

    fig, ax = plt.subplots(figsize=(8, 6))

    for i, f in enumerate(func):
        y = f(x)
        ax.plot(x, y, label=f"f{i}(x)", color=f"C{i}", linewidth=2)

    for px, py, label in points:
        ax.scatter(px, py, color="crimson", zorder=5)
        ax.annotate(
            label,
            (px, py),
            textcoords="offset points",
            xytext=(6, 6),
            fontsize=9,
        )

    if x_markers:
        xs = [m[1] for m in x_markers]
        ax.scatter(xs, [0] * len(xs), color="darkorange", marker="o", zorder=5)

        for i, x_val, ea in x_markers:
            ax.annotate(
                f"i={i}\nx={x_val:.4f}\nea={ea:.4f}",
                (x_val, 0),
                textcoords="offset points",
                xytext=(6, -25),
                fontsize=8,
                color="black",
            )

    ax.axhline(0, color="gray", linewidth=0.5)
    ax.axvline(0, color="gray", linewidth=0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    if title:
        ax.set_title(title)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()

def show_plots():
    plt.show()