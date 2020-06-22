import pickle
import settings
import os
import pandas as pd
import sklearn.metrics as metrics
from src.models.predict import HousePriceModel
from src.models.train_model import prepare_data
<<<<<<< HEAD
from src.data.pre_processing import clean_data
=======
>>>>>>> 5c2e135... Compute metrics for all models
import numpy as np


# Mean absolute percentage error (MAPE)
def mape(y_true: pd.Series, y_pred: pd.Series) -> float:
    """Compute Mean Absolute Percentage Error (MAPE)

    Args:
        y_true (pd.Series): actual values
        y_pred (pd.Series): predict values

    Returns:
        float: mape value
    """

    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


def evaluate_model(model_name: str, data: pd.DataFrame) -> dict:
    """Compute regression metrics for the model

    Args:
        model_name (str): name of the model folder
        data (pd.DataFrame): test data

    Returns:
        dict: A dict with all metrics
    """

    # Load models, and prepare the data
    model = HousePriceModel(model_name)
    data = clean_data(data, output_file='test-cleaned.csv')

    # Get inputs and target
    features = model.get_input_features()
    data = prepare_data(data)

    # Get inputs and target
    X_test = data[features]
    y_test = data['SalePrice']

    # Perform predictions and compute metrics
    y_pred = model.predict(X_test)

    results = {}
    results['mae'] = metrics.mean_absolute_error(y_test, y_pred)
    results['mse'] = metrics.mean_squared_error(y_test, y_pred)
    results['rmse'] = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    results['rmsle'] = np.sqrt(metrics.mean_squared_log_error(y_test, y_pred))
    results['r2'] = metrics.r2_score(y_test, y_pred)
    results['mape'] = mape(y_test, y_pred)

    return results


if __name__ == "__main__":

    test_df = pd.read_csv(os.path.join(settings.RAW_DATA_FOLDER, 'test.csv'))
    results_df = pd.DataFrame(columns=['Model', 'MAE', 'MSE', 'RMSE', 'R2', 'RMSLE', 'MAPE'])

    models = os.listdir(settings.MODELS_FOLDER)

    for model in models:

        if not os.path.isdir(os.path.join(settings.MODELS_FOLDER, model)):
            continue

        print(f'Evaluating model: {model}')
        # Compute and save the results
        results = evaluate_model(model, test_df)
        results_df.loc[len(results_df)] = [model, results['mae'], results['mse'], results['rmse'], results['r2'], results['rmsle'], results['mape']]

    # Sort results by RMSLE
    results_df = results_df.sort_values(by=['RMSLE'])

    print(results_df)
    report_path = os.path.join(settings.REPORTS_FOLDER, 'models_results.html')

    print(f"Report saved at: {report_path}")
    results_df.to_html(report_path)
