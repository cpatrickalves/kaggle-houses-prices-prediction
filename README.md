# Houses Prices Prediction

This project creates a Machine Learning model to estimate the price of a house based on a set in input features.

It was create from a Kaggle competition where te goal was to predict the final price of houses from 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa.

Data source: The [Ames Housing dataset](http://www.amstat.org/publications/jse/v19n3/decock.pdf) was compiled by Dean De Cock for use in data science education.

Competition page: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview

# Team

This project was developed by:

* [Patrick Alves](https://github.com/cpatrickalves/)
* [Igor Couto](https://github.com/igorccouto)
* [Renan Moura](https://github.com/renanmouraf)


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── submission     <- template to submit the solution to Kaggle.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── prepare_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tests              <- Tests scripts

--------

## Getting Started

To estimate the price of a house you need ...


### Prerequisites

To run this code, download Python 3 from [Python.org](https://www.python.org/). 

After installing Python, add the required package using pip installer:

```
pip install -r requirements.txt
```

### Usage

To run the aplication , execute:
```
python app.py
```

#### Example

[SOME SCREENSHOT OF THE WEB APP]


### Web application

You can also run this script as an [Streamlit](https://www.streamlit.io/) application:
```
streamlit run app.py
```
It will automatically open the browser and show the app.

You can also test a demo on Heroku Plataform: [URL FOR THE APP ](https://)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
