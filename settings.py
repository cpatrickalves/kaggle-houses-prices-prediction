import os


ROOT_FOLDER = os.getcwd()
# Data
DATA_FOLDER = os.path.join(ROOT_FOLDER, 'data')
RAW_DATA_FOLDER = os.path.join(DATA_FOLDER, 'raw')
PROCESSED_DATA_FOLDER = os.path.join(DATA_FOLDER, 'processed')
SUBMISSION_DATA_FOLDER = os.path.join(DATA_FOLDER, 'submission')
KAGGLE_DATA_FOLDER = os.path.join(DATA_FOLDER, 'from_kaggle')
REPORTS_FOLDER = os.path.join(ROOT_FOLDER, 'reports')

# Models
MODELS_FOLDER = os.path.join(ROOT_FOLDER, 'models')

if __name__ == '__main__':
    # Prints all settings variables of the project.
    variables = [v for v in dir() if not v.startswith("__") and v.isupper()]
    for v in variables:
        value = globals()[v]
        print('- %s::: %s' % (v, value) )