import time
import pandas as pd
import seaborn as sns
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


def plot_1_2() -> None:
    "Creates and saves the plot"


def simulate_capital_conversion(initial_natural_stock=100, conversion_rate=1.2, depletion=50, replenish_rate=25, depreciation_rate=0.005, simulation_duration=100):
    """
    Simulates a one-time extraction of natural capital at a given conversion rate into produced capital. 
    The produced capital then depreciates at a given rate and the natural capital converges asymtotically according to a replenish rate to its original value.
    """
    natural_capital = initial_natural_stock
    produced_capital = 0
    steps_to_go = simulation_duration
    print("Initial Natural Capital:", initial_natural_stock)
    print("Conversion Rate produced/natural:", conversion_rate)
    print("Depletion:", depletion)
    print("Replenish rate of natural capital:", replenish_rate)
    print("Depletion rate of produced capital:", depreciation_rate)
    print("Simulation duration:", simulation_duration)

    time_values = []
    natural_values = []
    produced_values = []
    combined_values = []

    while steps_to_go > 0:
        if steps_to_go == (simulation_duration-1):
            natural_capital -= depletion
            produced_capital = depletion*conversion_rate

        if natural_capital < 0:
            natural_capital = 0

        natural_capital += (natural_capital * replenish_rate) / \
            (natural_capital ** 2)
        produced_capital -= produced_capital * depreciation_rate
        time_values.append(simulation_duration-steps_to_go)
        natural_values.append(natural_capital)
        produced_values.append(produced_capital)
        combined_values.append(natural_capital+produced_capital)
        # Simulate time passing
        steps_to_go -= 1

        # Replenish Natural Capital

        if natural_capital > initial_natural_stock:
            natural_capital = initial_natural_stock

    # Create DataFrame for plotting
    df = pd.DataFrame({"Time": time_values, "Natural Capital": natural_values,
                      "Produced Capital": produced_values, "Total Capital": combined_values})

    # Plot using Seaborn
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # Plot natural capital
    sns.lineplot(data=df, x="Time", y="Natural Capital",
                 label="Natural Capital")

    sns.lineplot(data=df, x="Time", y="Produced Capital",
                 label="Produced Capital")

    sns.lineplot(data=df, x="Time", y="Total Capital",
                 label="Combined Capital")

    sns.lineplot(data=df, x="Time", y=initial_natural_stock,
                 label="Starting Capital")
    # Fill the space between the two curves
    plt.fill_between(df["Time"], df["Total Capital"], initial_natural_stock,
                     where=df["Total Capital"] >= initial_natural_stock, color="green", alpha=0.3)
    plt.fill_between(df["Time"], df["Total Capital"], initial_natural_stock,
                     where=df["Total Capital"] < initial_natural_stock, color="red", alpha=0.3)

    plt.title("Calculating extraction of natural to produced capital")
    plt.xlabel("Time")
    plt.ylabel("Capital Stock")
    plt.legend()
    plt.show()


def simulate_capital_extraction(initial_natural_stock=100, conversion_rate=1.2, extraction=0.005, replenish_rate=25, depletion_rate=0.005, simulation_duration=100):
    """
    Simulates a one-time extraction of natural capital at a given conversion rate into produced capital. 
    The produced capital then depreciates at a given rate and the natural capital converges asymtotically according to a replenish rate to its original value.
    """
    natural_capital = initial_natural_stock
    produced_capital = 0
    steps_to_go = simulation_duration
    print("Initial Natural Capital:", initial_natural_stock)
    print("Conversion Rate produced/natural:", conversion_rate)
    print("Extraction rate:", extraction)
    print("Replenish rate of natural capital:", replenish_rate)
    print("Depletion rate of produced capital:", depletion_rate)
    print("Simulation duration:", simulation_duration)

    time_values = []
    natural_values = []
    produced_values = []
    combined_values = []

    while steps_to_go > 0:
        if natural_capital < 0:
            natural_capital = 0
        produced_capital = (
            produced_capital+(natural_capital*extraction))*(1-depletion_rate)
        natural_capital += -(natural_capital*extraction) + (natural_capital * replenish_rate) / \
            (natural_capital ** 2)
        time_values.append(simulation_duration-steps_to_go)
        natural_values.append(natural_capital)
        produced_values.append(produced_capital)
        combined_values.append(natural_capital+produced_capital)
        # Simulate time passing
        steps_to_go -= 1

        # Replenish Natural Capital

        if natural_capital > initial_natural_stock:
            natural_capital = initial_natural_stock

    # Create DataFrame for plotting
    df = pd.DataFrame({"Time": time_values, "Natural Capital": natural_values,
                      "Produced Capital": produced_values, "Total Capital": combined_values})

    # Plot using Seaborn
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # Plot natural capital
    sns.lineplot(data=df, x="Time", y="Natural Capital",
                 label="Natural Capital")

    # Plot produced capital
    sns.lineplot(data=df, x="Time", y="Produced Capital",
                 label="Produced Capital")

    sns.lineplot(data=df, x="Time", y="Total Capital",
                 label="Combined Capital")

    sns.lineplot(data=df, x="Time", y=initial_natural_stock,
                 label="Starting Capital")
    # Fill the space between the two curves
    plt.fill_between(df["Time"], df["Total Capital"], initial_natural_stock,
                     where=df["Total Capital"] >= initial_natural_stock, color="green", alpha=0.3)
    plt.fill_between(df["Time"], df["Total Capital"], initial_natural_stock,
                     where=df["Total Capital"] < initial_natural_stock, color="red", alpha=0.3)

    plt.title("Calculating extraction of natural to produced capital")
    plt.xlabel("Time")
    plt.ylabel("Capital Stock")
    plt.legend()
    plt.show()

# Example usage
