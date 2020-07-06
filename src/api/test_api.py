from starlette.testclient import TestClient
from api import app
import requests
from src.models.predict import HousePriceModel


client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "online"}


def test_predict(): #FIXME: there is a warning in this test (numpy.ufunc size changed), I can't figure out how to fix it.
    """Send a request to the API using a sample from the model
       and evaluates the response.
    """
    model_dir = 'tree_model'
    # set the model saved at models
    model = HousePriceModel(model_dir)

    # Get one input example as dict
    test_df = model.get_input_example()
    sample_input = test_df.to_dict(orient='records')[0]

    response = client.post("/predict",json=sample_input)
    assert response.status_code == 200

    # Check if the response has the right data types
    try:
        response_schema = PredictReponse(**response.json())
    except:
        response_schema = None

    assert isinstance(response_schema, PredictReponse)



def run_prediction_from_sample(model_dir):
    """Send a request to the API using a sample from the model

    Args:
        model_dir (str): model folder
    """

    # set the model saved at models
    print(f"Loading model: {model_dir}")
    model = HousePriceModel(model_dir)

    # Get one input example as dict
    test_df = model.get_input_example()
    sample_input = test_df.to_dict(orient='records')[0]

    # Run send a predict request with the sample
    url="http://127.0.0.1:8000/predict"
    headers = {"Content-Type": "application/json", "Accept":"text/plain"}

    response = requests.post(url, headers=headers, json=sample_input)
    print(response.text)


if __name__ == "__main__":
    run_prediction_from_sample('tree_model')