import pickle
import os
import pandas as pd

def load_data(dataset_path):
    data = pd.read_csv(dataset_path)
    return data

def load_model(path, name):
    pkl_filename = os.path.join(path, name)

    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)

    return pickle_model

def main():
    model = load_model('./', 'tree_model')

if __name__ == '__main__':
    main()