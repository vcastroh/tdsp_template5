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


def prepare_data(data):
    data.isnull().sum()
    data.bmi[data.bmi.isnull()] = data.bmi.mean()
    data.bmi.isnull().sum()

    data.age = data.age.astype('int64')
    data['gender'].replace({'Male': 3, 'Female': 1, 'Other': 2}, inplace=True)
    data['gender'] = data['gender'].astype('uint8')

    data.hypertension = data.hypertension.astype('uint8')
    data.heart_disease = data.heart_disease.astype('uint8')

    label_encoder = LabelEncoder()
    data['smoking_status'] = label_encoder.fit_transform(data['smoking_status'])
    data.smoking_status = data.smoking_status.astype('uint8')

    data.ever_married[data.ever_married == 'Yes'] = 1
    data.ever_married[data.ever_married == 'No'] = 0
    data.ever_married = data.ever_married.astype('uint8')

    data.Residence_type[data.Residence_type == 'Rural'] = 1
    data.Residence_type[data.Residence_type == 'Urban'] = 0
    data.Residence_type = data.Residence_type.astype('uint8')

    work_type_dummies = pd.get_dummies(data['work_type'])
    data = pd.concat((data, work_type_dummies), axis=1)
    data.drop('work_type', axis=1, inplace=True)

    return data


def visualize_correlation(data):
    plt.figure(figsize=(15, 15))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')


def perform_split(data):
    y = data['stroke']
    data.drop('stroke', axis=1, inplace=True)

    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)

    train_x, val_x, train_y, val_y = train_test_split(data, y, test_size=0.25, random_state=1)
    return train_x, val_x, train_y, val_y


def model(train_x, train_y):
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(train_x, train_y)
    return rf_model


def evaluate_model(model, val_x, val_y):
    predictions = model.predict(val_x)
    print("Confusion Matrix:")
    print(confusion_matrix(val_y, predictions))
    print("Classification Report:")
    print(classification_report(val_y, predictions))
