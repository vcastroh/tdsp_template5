from load_data import load_data
from perform_eda import perform_eda
from prepare_data import prepare_data


def visualize_correlation(data):
    plt.figure(figsize=(15, 15))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')