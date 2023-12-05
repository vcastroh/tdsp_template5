import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


def load_data(file_path):
    data = pd.read_csv(file_path, index_col='id')
    return data

def perform_eda(data):
    print(data.shape)
    print(data.head(10))
    print(data.describe())
    sns.distplot(data.age)
    print(data.dtypes)
