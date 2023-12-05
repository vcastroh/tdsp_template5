from load_data import load_data
from perform_eda import perform_eda
from prepare_data import prepare_data
from visualize_correlation import visualize_correlation


def perform_split(data):
    y = data['stroke']
    data.drop('stroke', axis=1, inplace=True)

    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)

    train_x, val_x, train_y, val_y = train_test_split(data, y, test_size=0.25, random_state=1)
    return train_x, val_x, train_y, val_y