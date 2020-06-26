import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import Pipeline
import os
import pickle
from src.data import pre_processing
import settings


def load_data(dataset_path):
    print(f"Loading the data at {dataset_path}")
    data = pd.read_csv(dataset_path)
    return data


def remove_columns_small_correlation(train_data):
    corr_matrix = train_data.corr()
    correlations = corr_matrix["SalePrice"]
    uncorrelated_columns = correlations[correlations < 0.3]
    train_data = train_data.drop(columns=uncorrelated_columns.index)

    return train_data


def prepare_data(train_data):
    print(f"Performing data cleaning ...")
    train_data = pre_processing.clean_data(train_data)
    print(f"Performing feature selection ...")
    train_data = remove_columns_small_correlation(train_data)

    return train_data


def train_model(x_train, y_train):

    print("Training the model ...")

    model = Pipeline(steps=[
        ("label encoding", OneHotEncoder(handle_unknown='ignore')),
        ("tree model", DecisionTreeRegressor())
    ])
    model.fit(x_train, y_train)

    return model


def accuracy(model, x_test, y_test):
    print("Testing the model ...")
    predictions = model.predict(x_test)
    tree_mse = mean_squared_error(y_test, predictions)
    tree_rmse = np.sqrt(tree_mse)
    return tree_rmse


def export_model(model, inputs_df, output_dir='last_model', path=settings.MODELS_FOLDER):
    """Saves model as PKL file and an example of the input data as a CSV file

    Args:
        model (object): trained model
        inputs_df (DataFrame): a dataframe with a set of examples
        output_dir (str, optional): The directory where the files should be saved. Defaults to 'last_model'.
        path (str, optional): path where the output_dir should be created. Defaults to settings.MODELS_FOLDER.
    """

    # Create directory if not exist
    save_dir = os.path.join(path, output_dir)
    if not (os.path.exists(save_dir)):
        os.mkdir(save_dir)

    # Save the model
    pkl_path = os.path.join(save_dir, 'model.pkl')
    with open(pkl_path, 'wb') as file:
        pickle.dump(model, file)
        print(f"Model saved at {pkl_path}")

    # Save a set of examples of train data
    examples_path = os.path.join(save_dir, 'test_input.csv')
    inputs_df.to_csv(examples_path, index=False)
    print(f"Input examples saved at {examples_path}")


def main():
    print("-"*20, "Starting", "-"*20)
    # Load data
    train_data = os.path.join(settings.RAW_DATA_FOLDER, 'train.csv')
    train = load_data(train_data)
    train = prepare_data(train)

    # Split train test
    x_train = train.drop(columns=['SalePrice'])
    y_train = train['SalePrice']

    # Train and Test
    model = train_model(x_train, y_train)
    rmse = accuracy(model, x_train, y_train)

    print(f"RMSE: {rmse}")

    # Save the model and input data
    export_model(model, x_train.head(5), output_dir='tree_model')

    print("-"*20, "Done", "-"*20)

if __name__ == '__main__':
    main()