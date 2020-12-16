import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from config import data_path

print('imports success')

df = pd.read_excel(data_path, engine='openpyxl')
print(df)
