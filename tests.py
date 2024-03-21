import pandas as pd
from data import fix_data

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Creating a sample DataFrame with missing values ('None' and '') in 'artist' or 'song' columns
data = {
    'artist': ['John', 'None', '', 'Jane'],  # Using '' for missing values
    'song': ['Song 1', '', 'Song 3', 'Song 4'],  # Using '' for missing values
    'duration_ms': [200000, 250000, 180000, 220000],
    'year': [2020, 2021, 2022, 2023],
    'popularity': [80, None, 70, 90],  # Using None for missing values
    'danceability': [0.70, 0.85, 'None', ''],  # Using None for missing values
    'energy': [0.80, 0.75, 0.85, None]  # Using None for missing values
}

df_input = pd.DataFrame(data)
df_fixed = fix_data(df_input)

print(df_fixed)

data_expected_after_fix = {
    'artist': ['John', 'Jane'],
    'song': ['Song 1', 'Song 4'],
    'year': [2020, 2023],
    'popularity': [80.0, 90.0],
    'danceability': [70.0, 0.0],
    'energy': [80, 0.0],
    'duration_min': [3.33, 3.67],
    'avg_score': [76.67, 30.0]
}

df_expected_after_fix = pd.DataFrame(data_expected_after_fix)


if df_fixed.equals(df_expected_after_fix):
    print('Test completed successfully')
else:
    print('Test Failed')

#
# print('--------------------')
# print(df_fixed)
# print('--------------------')
# print(df_expected_after_fix)