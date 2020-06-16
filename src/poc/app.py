# Third-paty
import pandas as pd
import streamlit as st
# Project
import sys
sys.path.append('..')
from models import predict

model = predict.HousePriceModel(r'tree_model')


# Sidebar
st.sidebar.title('Input')
input_examples = model.get_input_example()
input_example = input_examples.sample().to_dict('r')

for i in input_example:
    for k, v in i.items():
        st.sidebar.number_input(k, value=v)

# Main panel
st.title('House Prices Preditor')
st.write('Predictor::')
st.write(model.predict(input_example))
