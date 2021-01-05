import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import customerSeg.config

class Transform:

    def __init__(self, df, target):
        self.df = df
        self.target = target
        self.customers = pd.DataFrame()

    def preprocess(self):
        """
        Remove rows with null 'CustomerID'.
        Keep only day of purchase from 'InvoiceDate' (remove timestamp).
        Create 'TotalSum' column containing purchase value ('UnitPrice' * 'Quantity').
        """
        self.df = self.df[self.df['CustomerID'].notna()]
        self.df['InvoiceDate'] = self.df['InvoiceDate'].dt.date
        self.df['TotalSum'] = self.df['Quantity'] * self.df['UnitPrice']

    def generate_customers_table(self):
        """
        For use with preprocessed data.
        Expects self.df columns [CustomerID, InvoiceDate, InvoiceNo, TotalSum].
        Creates 'Recency'. 'Frequency', and 'MonetaryValue' for each CustomerID.
        """
        snapshot_date = max(self.df['InvoiceDate']) + timedelta(days=1)
        self.customers = (self.df.groupby(['CustomerID'])
            .agg({'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
            'InvoiceNo': 'count',
            'TotalSum': 'sum'}))

        self.customers.rename(
            columns={'InvoiceDate': 'Recency',
                    'InvoiceNo': 'Frequency',
                    'TotalSum': 'MonetaryValue'},
            inplace=True)
    
    def save(self):
        self.customers.to_csv(self.target)

    def transform(self):
        self.preprocess()
        self.generate_customers_table()
        self.save()


if __name__ == "__main__":
    datapath = customerSeg.config.merged_data_path  # .../data/merged/merge.csv
    outpath = customerSeg.config.customer_table_path # .../data/transformed/customer_table.csv
    
    df = pd.read_csv(datapath)
    
    T = Transform(df=df, target=outpath)
    T.transform()