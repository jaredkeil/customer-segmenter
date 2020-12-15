# Customer Segmenter

## Data

From the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/online+retail)

This is a transactional data (23 mb) set for a UK-based and registered non-store online retail.


### Dependencies
- Data is in excel format, so **xlrd** package is required.
- Rest of the libraries are common: numpy, pandas, sklearn, matplotlib.

xlrd may be a worthwile install for you entire system, but starting with a clean python environment is always nice.

### Environment setup

First, `git clone` clone this repository.

Create a python virtual environment. Name of the environment as you like. In the example below, it is 'my_env':

    python -m venv my_env

Activate the environment:

    source my_env/bin/activate

Install dependencies
    
    pip install -r requirements.txt