from data import *
from functions import *
import pandas as pd

from data import *
from functions import *
import pandas as pd


class DataPopularity:
    def __init__(self, filename):
        self.filename = filename
        self.df = fix_data(load_data('songs_normalize.csv'))

    def plot_top_5_most_popular_songs(self):
        top_n_by_graph(self.df, 5, 'popularity')

    def print_artists_starting_with_letter(self, letter, saved_to_file=False):
        print(f'All artists in the DF that start with the letter {letter.upper()}')
        result_df = get_artists_starting_with_letter(self.df, letter)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files', f'artists_starting_with_letter_{letter.upper()}')

    def print_average_song_popularity_of_artist(self, artist_name):
        print(f'The average song popularity of {artist_name} is:')
        print(average_rating_per_artist_by_column(self.df, artist_name, 'popularity').iloc[0][
                  f'Avg_Songs_Rating_By_popularity'])

    def print_top_5_most_popular_songs_of_artist(self, artist_name):
        print(f'The top 5 most popular songs of {artist_name} are:')
        print(most_rated_song_for_artist_by_column(self.df, artist_name, 'popularity').head(5))

    def print_top_5_artists_by_average_song_popularity(self):
        print('Top 5 Artists by average song popularity:')
        print(artist_rank_by_column(self.df, 'popularity').head(5))

    def print_top_5_most_rated_song_per_artist(self):
        print('Top 5 artists and their most popular song:')
        print(most_rated_song_per_artist_by_column(self.df, 'popularity').head(5))

    def print_top_5_most_rated_songs_in_year(self, year):
        print(f'Top 5 most popular songs in the year {year}:')
        print(most_rated_in_year_by_column(self.df, year, 'popularity').head(5))

    def plot_most_popular_song_for_artist_in_every_year(self, artist_name='Eminem'):
        print(f'The most popular song for {artist_name} in every year they released a song, graphed:')
        print(artist_most_column_song_rank_over_the_years(self.df, artist_name, 'popularity'))


# ---------------------------------------------------------------------------------------------------------------------------

class DataDanceability:
    def __init__(self, filename):
        self.filename = filename
        self.df = fix_data(load_data('songs_normalize.csv'))

    def plot_top_5_most_danceable_songs(self):
        top_n_by_graph(self.df, 5, 'danceability')

    def print_artists_starting_with_letter(self, letter):
        print(f'All artists in DF that are starting with letter {letter.upper()}')
        print(get_artists_starting_with_letter(self.df, letter))

    def print_average_danceability_of_artist(self, artist_name):
        print(f'The average danceability of {artist_name} is:')
        print(average_rating_per_artist_by_column(self.df, artist_name, 'danceability').iloc[0][
                  f'Avg_Songs_Rating_By_danceability'])

    def print_top_5_most_danceable_songs_of_artist(self, artist_name):
        print(f'The top 5 most danceable songs of {artist_name} are:')
        print(most_rated_song_for_artist_by_column(self.df, artist_name, 'danceability').head(5))

    def print_top_5_artists_by_average_danceability(self):
        print('Top 5 Artists by average danceability:')
        print(artist_rank_by_column(self.df, 'danceability').head(5))

    def print_top_5_most_danceable_song_per_artist(self):
        print('Top 5 artists and their most danceable song:')
        print(most_rated_song_per_artist_by_column(self.df, 'danceability').head(5))

    def print_top_5_most_danceable_songs_in_year(self, year):
        print(f'Top 5 most danceable songs in year {year}:')
        print(most_rated_in_year_by_column(self.df, year, 'danceability').head(5))

    def plot_most_danceable_song_for_artist_in_every_year(self, artist_name='Eminem'):
        print(f'The most danceable song for {artist_name} in every year they released a song, graphed:')
        print(artist_most_column_song_rank_over_the_years(self.df, artist_name, 'danceability'))


# ---------------------------------------------------------------------------------------------------------------------------

class DataEnergy:
    def __init__(self, filename):
        self.filename = filename
        self.df = fix_data(load_data('songs_normalize.csv'))

    def plot_top_5_most_energetic_songs(self):
        top_n_by_graph(self.df, 5, 'energy')

    def print_artists_starting_with_letter(self, letter):
        print(f'All artists in the DF that start with the letter {letter.upper()}')
        print(get_artists_starting_with_letter(self.df, letter))

    def print_average_energy_of_artist(self, artist_name):
        print(f'The average energy of {artist_name} is:')
        print(average_rating_per_artist_by_column(self.df, artist_name, 'energy').iloc[0][
                  f'Avg_Songs_Rating_By_energy'])

    def print_top_5_most_energetic_songs_of_artist(self, artist_name):
        print(f'The top 5 most energetic songs of {artist_name} are:')
        print(most_rated_song_for_artist_by_column(self.df, artist_name, 'energy').head(5))

    def print_top_5_artists_by_average_energy(self):
        print('Top 5 Artists by average energy:')
        print(artist_rank_by_column(self.df, 'energy').head(5))

    def print_top_5_most_energetic_song_per_artist(self):
        print('Top 5 artists and their most energetic song:')
        print(most_rated_song_per_artist_by_column(self.df, 'energy').head(5))

    def print_top_5_most_energetic_songs_in_year(self, year):
        print(f'Top 5 most energetic songs in the year {year}:')
        print(most_rated_in_year_by_column(self.df, year, 'energy').head(5))

    def plot_most_energetic_song_for_artist_in_every_year(self, artist_name='Britney Spears'):
        print(f'The most energetic song for {artist_name} in every year they released a song, graphed:')
        print(artist_most_column_song_rank_over_the_years(self.df, artist_name, 'energy'))
