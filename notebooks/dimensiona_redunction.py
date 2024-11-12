# Numpy for numercal computing
import numpy as np

# pandas for dataframes
import pandas as pd

# increase Pandas Max Display columns
# pd.set_option('display.max_colunns', 100)
pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", 100)
pd.set_option("display.width", 100)
pd.set_option("max_colwidth", 100)

# read cleaned_transactions.csv
tx_df = pd.read_csv("cleaned_transactions.csv")
