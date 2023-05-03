import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Given list of label and count tuples, plot bar chart sorted on descending count from left to right
def plot_bars(labels_counts, title, xlabel, ylabel, save=False, filename='plot.png'):
    labels_counts.sort(key=lambda x: x[1], reverse=True)
    labels = [el[0] for el in labels_counts]
    counts = [el[1] for el in labels_counts]
    fig, ax = plt.subplots()
    plt.grid(zorder=0)
    ax.bar(labels, counts, zorder=3)
    ax.set_title(f'Counts: {title}')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_yscale('log')

    # Format y-axis labels to not be in scientific notation
    ax.yaxis.set_major_formatter(mticker.ScalarFormatter())

    if save:
        plt.savefig(f'img/{filename}')
    else:
        plt.show()


# Given list counts, sort in ascending order based on counts and plot cumulative distribution
def plot_cumulative(counts, title, save=False, filename='plot.png'):
    counts.sort()
    data = np.cumsum(counts)
    total = np.sum(counts)

    y = data / total

    x = np.linspace(0, 1, len(y))

    fig, ax = plt.subplots()
    plt.grid()
    ax.plot(x, y)
    ax.set_title(f'Size distribution: {title}')
    # ax.set_xlabel(xlabel)
    ax.set_ylabel('Cumulative distribution')

    if save:
        plt.savefig(f'img/{filename}')
    else:
        plt.show()
