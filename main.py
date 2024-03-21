from data import load_data, fix_data
import pandas as pd

# Adjust display settings to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


df = load_data()
df = pd.DataFrame(fix_data(df))

print(df.head(2))
