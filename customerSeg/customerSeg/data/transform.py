import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def customer_table(df):
    """
    For use with preprocessed data.
    Expects columns CustomerID, InvoiceDate, InvoiceNo, TotalSum
    df : pd.DataFrame
    """
    snapshot_date = max(df['InvoiceDate']) + timedelta(days=1)
    customers = (df.groupby(['CustomerID'])
        .agg({'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'count',
        'TotalSum': 'sum'}))

    customers.rename(columns = {'InvoiceDate': 'Recency',
                                'InvoiceNo': 'Frequency',
                                'TotalSum': 'MonetaryValue'}, inplace=True)

    return customers
                                

if __name__ == "__main__":
    from customerSeg.config import data_dir, interim_dir
    df = pd.read_csv(raw_dir)
    