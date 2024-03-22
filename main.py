from data import *
from functions import *
import pandas as pd

# Adjust display settings to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Load the csv file into DF:
df = load_data()

# Fix the data by needed standard:
df = pd.DataFrame(fix_data(df))

# Generate the graph for the top 5 songs by 'avg_score'
top_n_by_graph(df, 5, 'avg_score')

# Print the average song popularity of Eminem:
print('---------------------------------------------------------')
print('The average song popularity of Eminem: ')
print(avg_per_artist(df, 'Eminem', 'popularity'))
print('---------------------------------------------------------')

# Print the average song danceability of Britney:
print('---------------------------------------------------------')
print('The average song danceability of Britney Spears: ')
print(avg_per_artist(df, 'Britney Spears', 'danceability'))
print('---------------------------------------------------------')

# print top 3 Artists by average songs popularity:
print('---------------------------------------------------------')
artist_by_avg_songs_popularity_df = artist_rank_by_column(df, 'popularity')
print('Top 3 Artists by average songs popularity')
print(artist_by_avg_songs_popularity_df.head(3))
print('---------------------------------------------------------')

# print top 3 Artists by average songs danceability:
print('---------------------------------------------------------')
artist_by_avg_songs_danceability_df = artist_rank_by_column(df, 'danceability')
print('Top 3 Artists by average songs danceability')
print(artist_by_avg_songs_danceability_df.head(3))
print('---------------------------------------------------------')
