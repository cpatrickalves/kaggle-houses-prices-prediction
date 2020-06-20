# Houses Prices Prediction

This project creates a Machine Learning model to estimate the price of a house based on a set in input features.

It was created from a Kaggle competition where the goal was to predict the final price of houses from 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa.

Data source: The [Ames Housing dataset](http://www.amstat.org/publications/jse/v19n3/decock.pdf) was compiled by Dean De Cock for use in data science education.

Competition page: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview

# Guide-questions

It's important to answer some guide-questions before starting any Data Science project.

1. **Which problem do we want to solve?** Predict house prices based in more than a hundred of aspects (variables).

2. **Why this project is important?** Guide buyers/sellers to pay/demand fair house prices.

3. **How the solution of this project will be used in practice?** When clients offer their houses on our site, they can be oriented to increase or decrease their offers to keep them competitive.

4. **Does the previous question help to understand the limits to put the solution into production?** It's necessary to select which aspects of a house (feature selection) are more important to predict the price of an offer. The dataset has 163 variables. Besides becoming a "heavy" model to use in production, no client will feel comfortable filling a form with this amount of fields to use this service.

5. **Which value does it generate to business?** In general, buyers or sellers don't have any idea how much they could pay or demand in an offer for a house. This service can be attractive to clients that don't know the real state market. It can be a non-free service.

6. **How do we measure the success or failure of this project?** We can count how many clients demand this service over the total amount of offers on the site. If the service is non-free, how much revenue can be generated?

7. **Which are the metrics of business/products we will affect?**
 - Primary metrics: Clients that use the service / total clients
 - Secondary metrics: Increase in revenue after activating the service.

8. **Which is the metric to evaluate the model?** To measure the performance between developed models, we will use [Root Mean Squared Logarithmic Error (RMSLE)](https://www.kaggle.com/c/ashrae-energy-prediction/discussion/113064) and the goal is to reach a **RMSLE lower than 0.1**.

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
    │   ├── from_kaggle    <- original files from kaggle website.
    │   ├── submission     <- template to submit the solution to Kaggle.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original "train.csv" data from Kaggle splitted in train and test.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. A naming convention is a number (for ordering),
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
    │   └── visualization  <- Scripts to create exploratory and results-oriented visualizations
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

If you are using Pipenv:
```
pipenv install 
```

### Usage

To run the application, execute:
```
python app.py
```

#### For developers

If you are usin Pipenv, there are some packages used specific for development (ex: pytest)
To install them use:
```
pipenv install --dev
```
Then, run pytest to make sure everything is fine.
```
pytest
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
