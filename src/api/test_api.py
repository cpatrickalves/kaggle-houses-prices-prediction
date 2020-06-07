from starlette.testclient import TestClient
from api import app
import requests

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "online"}

def test_predict():
    response = client.post(
        "/predict",
        json={"SaleType": "foobar",
              "OpenPorchSF": "Foo Bar",
              "SaleCondition": "The Foo Bar"},
    )
    assert response.status_code == 200
    assert response.json() == {"SalesPrice": 42}


def run_prediction_from_sample(model_dir):
    """Send a request to the API using a sample from the model

    Args:
        model_dir (str): model folder
    """

    # set the model saved at models
    #logger.info(f"Loading model: {model_dir}")
    #model = HousePriceModel(model_dir)

    # Get one input example as dict
    #test_df = model.get_input_example()
    #sample_input = test_df.to_dict(orient='records')[0]

    # Run send a predict request with the sample
    url="http://127.0.0.1:8000/predict"
    headers = {"Content-Type": "application/json", "Accept":"text/plain"}
    sample_input = {"SaleType": "Somevalue01", "WoodDeckSF": "42", "SaleCondition":22}
    response = requests.post(url, headers=headers, json=sample_input)
    print(response.text)


if __name__ == "__main__":
    run_prediction_from_sample('tree_model')
