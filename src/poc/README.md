# How to see the Proof of Concept (POC)

To see the POC (a streamlit app), please:

1. Install streamlit using requirements.txt or pipenv.
2. Run models/train_model.py to create an pkl file in tree_model.
3. On poc folder, type:
```
$ streamlit run app.py
```

By default, the application already loads a valid input choosing (randomly) a line of tree_model/test_input.csv.
