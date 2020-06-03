# Built-in
import os
# Third-party
import pandas as pd


def clean_data(df):
    """Makes an initial clean in a dataframe.

    Args:
        df (pd.DataFrame): A dataframe to clean.

    Returns:
        pd.DataFrame: the cleaned dataframe.
    """

    #### Please refer to the notebook 1.0-Exploratory-Data-Analysis.ipynb to more details

    # Removes columns with missing values issues
    cols_to_be_removed = ['Id', 'PoolQC', 'MiscFeature', 'Alley', 'Fence', 'LotFrontage', 'GarageYrBlt', 'MasVnrArea']
    df.drop(columns=cols_to_be_removed, inplace=True)

    # Transforms ordinal columns to numeric
    ordinal_cols = ['FireplaceQu', 'ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond', 'HeatingQC', 'KitchenQual', 'GarageQual', 'GarageCond']
    for col in ordinal_cols:
        df[col].fillna(0, inplace=True)
        df[col].replace({'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5}, inplace=True)

    # Fills NA where incorrectly pandas placed NaN
    for c in ['GarageType', 'GarageFinish', 'BsmtFinType2', 'BsmtExposure', 'BsmtFinType1']:
        df[c].fillna('NA', inplace=True)

    # Fills None where incorrectly pandas placed NaN
    df['MasVnrType'].fillna('None', inplace=True)

    # Imputes with most frequent value
    df['Electrical'].fillna('SBrkr', inplace=True)

    # Saves a copy
    df.to_csv('../../data/processed/train-cleaned.csv')

    return df

if __name__ == "__main__":
    train_file = '../../data/raw/train.csv'
    if os.path.exists(train_file):
        df = pd.read_csv(train_file)
        print('Raw::', df.shape)
        cleaned_df = clean_data(df)
        print('Cleaned::', cleaned_df.shape)
    else:
        print('File not found:', train_file)