import matplotlib.pyplot as plt
from supervenn import supervenn


def plot_1_1() -> None:
    "Creates and saves the plots"
    # Set figure size and coloring
    plt.figure(figsize=(8, 4))
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Accent.colors)
    sets = [
        {2, 3, 4, 5, 6, 7, },
        {2},
        {3, 4, 5, 6, 7, },
        {3},
        {4, 5, 6, 7, },
        {4},
        {5, 6, 7},
        {5},
        {6},
        {7},
    ]
    labels = ["Human Activity", "Non-Economic Activity",  "Economic Activity", "Services", "Assets",
              "Enabling Assets", "Capital", "Human", "Produced", "Natural"]
    supervenn(sets, labels, side_plots=False,
              min_width_for_annotation=1000, sets_ordering="size", reverse_sets_order=False, )
    plt.savefig(fname="Supervenn.png")
    plt.show()
