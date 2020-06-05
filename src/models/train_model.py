import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
import os
import pickle

import sys
sys.path.append('../')

from data import pre_processing

def load_data(dataset_path):
    data = pd.read_csv(dataset_path)
    return data

def remove_columns_small_correlation(train_data):
    corr_matrix = train_data.corr()

    correlations = corr_matrix["SalePrice"]

    uncorrelated_columns = correlations[correlations < 0.3]

    train_data = train_data.drop(columns=uncorrelated_columns.index)

    return train_data

def encode_categorical_columns(train_data):
    categorical_mask = train_data.dtypes==object

    categorical = train_data.columns[categorical_mask].tolist()

    le = LabelEncoder()

    train_data[categorical] = train_data[categorical].apply(lambda col: le.fit_transform(col))

    return train_data

def prepare_data(train_data):
    train_data = pre_processing.clean_data(train_data)
    train_data = remove_columns_small_correlation(train_data)
    train_data = encode_categorical_columns(train_data)

    return train_data

def save_data(dataframe, path, name):
    dataframe.to_csv(os.path.join(path, name), index=False)

def train_model(x_train, y_train):
    tree_reg = DecisionTreeRegressor()
    tree_reg.fit(x_train, y_train)
    
    return tree_reg

def accuracy(model, x_test, y_test):
    predictions = model.predict(x_test)
    tree_mse = mean_squared_error(y_test, predictions)
    tree_rmse = np.sqrt(tree_mse)
    return tree_rmse

def export_model(model, path, name):
    pkl_filename = os.path.join(path, name)

    with open(pkl_filename, 'wb') as file:
        pickle.dump(model, file)

def main():
    train = load_data('../../data/raw/train.csv')

    train = prepare_data(train)

    x_train = train.drop(columns=['SalePrice'])
    y_train = train['SalePrice']

    model = train_model(x_train, y_train)

    rmse = accuracy(model, x_train, y_train)

    print(rmse)

    export_model(model, './', 'tree_model.pkl')
    
    save_data(x_train.head(5), './', 'test_input.csv')

if __name__ == '__main__':
    main()