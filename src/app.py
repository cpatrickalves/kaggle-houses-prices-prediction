# Third-paty
import pandas as pd
import streamlit as st
# Project
from models import predict

model = predict.HousePriceModel(r'D:\Dropbox\ds_pratica\kaggle-houses-prices-prediction\models\tree_model')


# Sidebar
st.sidebar.title('Input')
input_examples = model.get_input_example()
input_example = input_examples.sample().to_dict('list')

for k, v in input_example.items():
    st.sidebar.number_input(k, value=v[0])

# Main panel
st.title('House Prices Preditor')
st.write('Predictor::')
st.write(model.predict(input_example))
