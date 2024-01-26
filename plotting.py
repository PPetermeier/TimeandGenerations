import seaborn as sns
import matplotlib.pyplot as plt
from supervenn import supervenn


def plot_1_1():
    # Set figure size and coloring
    plt.figure(figsize=(8, 4))
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Accent.colors)
    sets = [
        {8},
        {7},
        {6},
        {5, 6, 7, 8},
        {4},
        {3, 4, 5, 6, 7, 8},
        {2, 3, 4, 5, 6, 7, 8},
        {1, 2, 3, 4, 5, 6, 7, 8},
    ]
    sets.reverse()
    labels = ["Human Activity", "Services", "Assets",
              "Enabling Assets", "Capital", "Human", "Produced", "Social"]
    supervenn = supervenn(sets, labels, side_plots=False,
                          min_width_for_annotation=1000, sets_ordering="size", reverse_sets_order=False, )
    plt.savefig(fname="Supervenn.png")
    plt.show()