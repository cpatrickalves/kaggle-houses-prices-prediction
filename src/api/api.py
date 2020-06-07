from fastapi import FastAPI
import pandas as pd
from logzero import logger
from pydantic import BaseModel
from typing import Dict
import json
import sys
sys.path.append('../')
from models import predict


# ------------------------ HOW TO USE ------------------------ #
# To see API documentation, start the API and access:
# <IPADDRESS>:8000/docs
# or
# <IPADDRESS>:8000/redoc
# or
# <IPADDRESS>:8000/openapi.json

app = FastAPI()

logger.info("API started")

#TODO: Use BaseModel for automatic validation
#class JsonBody(BaseModel):
#    name: str

# Create a Basemodel from dict?
#class ModelInputs(BaseModel):
#    SaleType : str = None
#    OpenPorchSF : str = None
#    WoodDeckSF : str = None
#    SaleCondition : str = None

@app.get("/")
def root():
    """
    Root view returns the system status
    """
    return {"status": "online"}


@app.post("/predict")
def predict(inputs: dict):

    #logger.info(f"API - POST /predict: \n {json.dumps(inputs, indent=4)}")

    # set the model saved at models/
    model_dir = 'tree_model'

    #print(f"Loading model: {model_dir}")
    #model = HousePriceModel(model_dir)

    # Get one input example as dict
    #test_df = model.get_input_example()
    #sample_input = test_df.to_dict(orient='records')[0]

    #input_features = model.get_input_features()
    #response = f"Prediction: {model.predict(sample_input)}")

    #return response
    return inputs
