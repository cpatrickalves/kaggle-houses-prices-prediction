import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
import os
import pickle

def load_data(dataset_path):
    data = pd.read_csv(dataset_path)
    return data

def find_remove_missing_columns(train_data, test_data):
    missing_val_count_by_column = (train_data.isnull().sum())
    removed_columns_nan = missing_val_count_by_column[missing_val_count_by_column > 0]

    test_missing_val_count_by_column = (test_data.isnull().sum())
    test_removed_columns_nan = test_missing_val_count_by_column[test_missing_val_count_by_column > 0]

    total_columns_remove_nan = test_removed_columns_nan + removed_columns_nan

    train_without_missing_values = train_data.drop(columns=total_columns_remove_nan.index)

    test_without_missing_values = test_data.drop(columns=total_columns_remove_nan.index)

    return train_without_missing_values, test_without_missing_values

def remove_columns_small_correlation(train_data, test_data):
    corr_matrix = train_data.corr()

    correlations = corr_matrix["SalePrice"]

    uncorrelated_columns = correlations[correlations < 0.3]

    train_data = train_data.drop(columns=uncorrelated_columns.index)
    test_data = test_data.drop(columns=uncorrelated_columns.index)

    return train_data, test_data

def encode_categorical_columns(train_data, test_data):
    categorical_mask = train_data.dtypes==object

    categorical = train_data.columns[categorical_mask].tolist()

    le = LabelEncoder()

    train_data[categorical] = train_data[categorical].apply(lambda col: le.fit_transform(col))

    test_categorical_mask = test_data.dtypes==object

    test_categorical = test_data.columns[test_categorical_mask].tolist()

    le_test = LabelEncoder()

    test_data[test_categorical] = test_data[test_categorical].apply(lambda col: le_test.fit_transform(col))

    return train_data, test_data

def clean_data(train_data, test_data):
    train_data, test_data = find_remove_missing_columns(train_data, test_data)
    train_data, test_data = remove_columns_small_correlation(train_data, test_data)
    train_data, test_data = encode_categorical_columns(train_data, test_data)

    return train_data, test_data

def save_data(dataframe, path, name):
    dataframe.to_csv(os.path.join(path, name))

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

    pass

def main():
    train = load_data('../../data/raw/train.csv')
    test = load_data('../../data/raw/test.csv')

    train, test = clean_data(train, test)

    x_train = train.drop(columns=['SalePrice'])
    y_train = train['SalePrice']

    model = train_model(x_train, y_train)

    rmse = accuracy(model, x_train, y_train)

    print(rmse)

    export_model(model, './', 'tree_model')

if __name__ == '__main__':
    main()