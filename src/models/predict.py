import pickle
import os
import pandas as pd
from train_model import load_data

class HousePriceModel():
    def __init__(self, model):
        self.model = model
        self.preds = None

    def predict(self, data):
        dataDF = pd.DataFrame.from_dict(data)
        self.preds = self.model.predict(dataDF)
        return self.preds

    
def load_model(path, name):
    pkl_filename = os.path.join(path, name)

    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)

    return pickle_model

def main():
    model_pkl = load_model('./', 'tree_model.pkl')
    model = HousePriceModel(model_pkl)
    test = load_data('./test_input.csv')
    print(model.predict(test.to_dict()))

if __name__ == '__main__':
    main()