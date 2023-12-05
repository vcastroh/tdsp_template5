from load_data import load_data
from perform_eda import perform_eda
from prepare_data import prepare_data
from visualize_correlation import visualize_correlation
from perform_split import perform_split


def model(train_x, train_y):
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(train_x, train_y)
    return rf_model