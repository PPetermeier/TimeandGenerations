import matplotlib.pyplot as plt
from supervenn import supervenn


def plot_1_1() -> None:
    "Creates and saves the plots"
    # Set figure size and coloring
    plt.figure(figsize=(8, 4))
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Accent.colors)
    sets = [
        {6},
        {5},
        {4},
        {4, 5, 6},
        {3},
        {3,  4, 5, 6},
        {2, },
        {1, 2, 3, 4, 5, 6},
    ]
    sets.reverse()
    labels = ["Human Activity", "Services", "Assets",
              "Enabling Assets", "Capital", "Human", "Produced", "Social"]
    supervenn(sets, labels, side_plots=False,
              min_width_for_annotation=1000, sets_ordering="size", reverse_sets_order=False, )
    plt.savefig(fname="Supervenn.png")
