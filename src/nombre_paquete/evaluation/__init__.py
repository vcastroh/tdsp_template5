from load_data import load_data
from perform_eda import perform_eda
from prepare_data import prepare_data
from visualize_correlation import visualize_correlation
from perform_split import perform_split
from model import model


def evaluate_model(model, val_x, val_y):
    predictions = model.predict(val_x)
    print("Confusion Matrix:")
    print(confusion_matrix(val_y, predictions))
    print("Classification Report:")
    print(classification_report(val_y, predictions))