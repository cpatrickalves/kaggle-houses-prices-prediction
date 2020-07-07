import os
import settings
import pandas as pd
from src.models.evaluate_models import evaluate_model


def test_all_models():
    """This test load all models, perform predictions with some examples of
       the test set and evaluate if the results are acceptable
    """

    # Test with 10 examples
    test_df = pd.read_csv(os.path.join(settings.RAW_DATA_FOLDER, 'test.csv')).head(10)
    results_df = pd.DataFrame(columns=['Model', 'MAE', 'MSE', 'RMSE', 'R2', 'RMSLE', 'MAPE'])

    models = os.listdir(settings.MODELS_FOLDER)

    for model in models:

        if not os.path.isdir(os.path.join(settings.MODELS_FOLDER, model)):
            continue

        # Compute and save the results
        results = evaluate_model(model, test_df)

        # Check if the R2 is above 70%
        assert results['r2'] > 0.7