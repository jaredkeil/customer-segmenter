import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
import pandas as pd

from customerSeg.config import transformed_dir

customer_data_path = transformed_dir
customer_df = pd.read_csv()

def analyze_skewness(x):
    """Visualize basic data transformations' effect on skewness of distribution.
    Performs (seperately) log-scaling, sqrt-scaling, and box-cox transform.

    x : str
        column name in customers, e.g. 'Recency', 'Frequency'
    """
    fig, ax = plt.subplots(2, 2, figsize=(5,5))
    sns.distplot(customer_df[x], ax=ax[0,0])
    sns.distplot(np.log(customer_df[x]), ax=ax[0,1])
    sns.distplot(np.sqrt(customer_df[x]), ax=ax[1,0])
    sns.distplot(stats.boxcox(customer_df[x])[0], ax=ax[1,1])
    plt.tight_layout()
    plt.show()
    
    print(customer_df[x].skew().round(2))
    print(np.log(customer_df[x]).skew().round(2))
    print(np.sqrt(customer_df[x]).skew().round(2))
    print(pd.Series(stats.boxcox(customer_df[x])[0]).skew().round(2))