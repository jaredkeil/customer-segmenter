# Customer Segmenter

## Data

From the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/online+retail)

This is a transactional data (23 mb) set for a UK-based and registered non-store online retail.


### Dependencies/Environment
To set up a virtual environment so all modules and scripts work out of the box:

From the repository root, run

    pipenv install

If you wish to not set up a virtual environment, and just run the bare minimum of the work found in the notebooks(primarily in notebook '1.0'):

- Data is in **.xlsx** format, so **openpyxl** package is required.
    - Note: as of xlrd v2.0.1 (Dec 2020), [xlrd](https://pypi.org/project/xlrd/) no longer reads .xlsx format, only pure .xls
- Rest of the libraries are common: numpy, pandas, sklearn, and matplotlib

Openpyxl may be a worthwile install for you entire system, but starting with a clean python environment is always nice.