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
print('------------------------------------------------------------------------------------------------------------')
print('The average song popularity of Eminem:')
print(average_rating_per_artist_by_column(df, 'Eminem', 'popularity'))
print('------------------------------------------------------------------------------------------------------------')

# Print the average song danceability of Britney Spears:
print('------------------------------------------------------------------------------------------------------------')
print('The average song danceability of Britney Spears:')
print(average_rating_per_artist_by_column(df, 'Britney Spears', 'danceability'))
print('------------------------------------------------------------------------------------------------------------')

# print top 3 Artists by average songs popularity:
print('------------------------------------------------------------------------------------------------------------')
artist_by_avg_songs_popularity_df = artist_rank_by_column(df, 'popularity')
print('Top 3 Artists by average songs popularity:')
print(artist_rank_by_column(df, 'popularity').head(3))
print('------------------------------------------------------------------------------------------------------------')

# print top 3 Artists by average songs danceability:
print('------------------------------------------------------------------------------------------------------------')
print('Top 3 Artists by average songs danceability:')
print(artist_rank_by_column(df, 'danceability').head(3))
print('------------------------------------------------------------------------------------------------------------')

print('------------------------------------------------------------------------------------------------------------')
# Print the top 3 songs by popularity by Eminem:
print('Top 3 songs by popularity by Eminem:')
print(most_rated_song_for_artist_by_column(df, 'Eminem', 'popularity').head(3))
print('------------------------------------------------------------------------------------------------------------')

print('------------------------------------------------------------------------------------------------------------')
# Print the top 3 songs by danceability by JAY-Z:
print('Top 3 songs by danceability by JAY-Z:')
print(most_rated_song_for_artist_by_column(df, 'JAY-Z', 'danceability').head(3))
print('------------------------------------------------------------------------------------------------------------')

print('------------------------------------------------------------------------------------------------------------')
# Print the top 3 artists and their most popular song:
print('Top 3 artists and their most popular song:')
print(most_rated_song_per_artist_by_column(df, 'popularity').head(3))
print('------------------------------------------------------------------------------------------------------------')

print('------------------------------------------------------------------------------------------------------------')
# Print the top 3 popular song in year 2007:
print('Top 3 popular song in year 2007:')
print(most_rated_in_year_by_column(df, 2007, 'popularity').head(3))
print('------------------------------------------------------------------------------------------------------------')

print('------------------------------------------------------------------------------------------------------------')
# Print the most popular song for Eminem in every year he realized a song and make a graph out of it:
print('the most popular song for Eminem in every year he realized a song and make a graph out of it')
print(artist_most_column_song_rank_over_the_years(df, 'Eminem', 'popularity'))
print('------------------------------------------------------------------------------------------------------------')

