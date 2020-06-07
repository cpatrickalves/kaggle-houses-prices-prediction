import pickle
import os
import pandas as pd

class HousePriceModel():

    def __init__(self, model_dir, models_path='../../models'):
        """Create the HousePriceModel object

        Args:
            model_dir (str): directory where the model is stored
            models_path (str): path to models directory
        """
        self.path = os.path.join(models_path, model_dir)
        self.model = self.load_model()
        self.preds = None

    def load_model(self):
        pkl_filename = os.path.join(self.path, 'model.pkl')

        try:
            with open(pkl_filename, 'rb') as file:
                pickle_model = pickle.load(file)
        except:
            print(f'Error loading the model at {pkl_filename}')
            return None

        return pickle_model

    def predict(self, data):
        dataDF = pd.DataFrame.from_dict(data)
        self.preds = self.model.predict(dataDF)
        return self.preds

    def get_input_example(self):
        """Get an input example for the model

        Returns:
            Dataframe: a dataframe with a set of examples
        """
        input_template = os.path.join(self.path, "test_input.csv")
        input_example = pd.read_csv(input_template)

        return input_example

    def get_input_features(self):
        """Get the input features for the model

        Returns:
            list: a list with all features expected by the model
        """
        input_features = self.get_input_example().columns

        return list(input_features)


def main():

    model_dir = 'tree_model'

    print(f"Loading model: {model_dir}")
    model = HousePriceModel(model_dir)
    test = model.get_input_example()

    input_features = model.get_input_features()
    print(f"Input features: {input_features}")
    print(f"Predictions: {model.predict(test.to_dict())}")

if __name__ == '__main__':
    main()