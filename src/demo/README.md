# Project Demo

To see the demonstration of the model as a web application, please:

1. Install streamlit using requirements.txt or pipenv.
2. Run models/train_model.py to create a pkl file in tree_model.
3. On `src/demo` folder, type:
```
$ streamlit run app.py
```

By default, the application already loads a valid input choosing (randomly) a line of tree_model/test_input.csv.
