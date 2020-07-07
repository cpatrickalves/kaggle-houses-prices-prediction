from pydantic import BaseModel
from typing import Dict


class PredictReponse(BaseModel):
    prediction: float
    duration: float = None # TODO: add analitics


#TODO: Use BaseModel for automatic validation
#class JsonBody(BaseModel):
#    name: str

# Create a Basemodel from dict? Use create_model()
#class ModelInputs(BaseModel):
#    SaleType : str = None
#    OpenPorchSF : str = None
#    WoodDeckSF : str = None
#    SaleCondition : str = None
#print(ModelInputs.schema_json(indent=2))
