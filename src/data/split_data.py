import os
import settings
import pandas as pd

def create_train_test_data(path_to_csv=None):
    """Split the data in train and test dataframes

    Args:
        df (pd.DataFrame): A dataframe to clean.

    Returns:
        tuple : a tuple with dataframes for train and test.
    """
    # load and split the data
    if path_to_csv:
        dataset = pd.read_csv(os.path.join(path_to_csv))
    else:
        dataset = pd.read_csv(os.path.join(settings.KAGGLE_DATA_FOLDER, 'train.csv'))

    data_train = dataset.sample(frac=0.8, random_state=42).reset_index(drop=True)
    data_test = dataset.drop(data_train.index).reset_index(drop=True)

    # save the data
    data_train.to_csv(os.path.join(settings.RAW_DATA_FOLDER, 'train.csv'), index=False)
    data_test.to_csv(os.path.join(settings.RAW_DATA_FOLDER, 'test.csv'), index=False)

    print("Train data for modeling: " + str(data_train.shape))
    print("Test data for predictions: " + str(data_test.shape))


if __name__ == "__main__":
    create_train_test_data()