from data import *
from functions import *


class DataPopularity:
    def __init__(self, filename):
        self.filename = filename
        self.df = fix_data(load_data('songs_normalize.csv'))

    def plot_top_5_most_popular_songs(self, saved_to_file=False):
        result_df = top_n_by_graph(self.df, 5, 'popularity')

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/popularity', f'top_5_most_popular_songs')

    def print_artists_starting_with_letter(self, letter, saved_to_file=False):
        print(f'All artists in the DF that start with the letter {letter.upper()}')
        result_df = get_artists_starting_with_letter(self.df, letter)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/popularity', f'artists_starting_with_letter_{letter.upper()}')

    def print_average_song_popularity_of_artist(self, artist_name):
        print(f'The average song popularity of {artist_name} is:')
        result_df = average_rating_per_artist_by_column(self.df, artist_name, 'popularity').iloc[0][
            f'Avg_Songs_Rating_By_popularity']
        print(result_df)

    def print_top_5_most_popular_songs_of_artist(self, artist_name, saved_to_file=False):
        print(f'The top 5 most popular songs of {artist_name} are:')
        result_df = most_rated_song_for_artist_by_column(self.df, artist_name, 'popularity').head(5)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/popularity', f'top_5_most_popular_songs_of_{artist_name}')

    def print_top_5_artists_by_average_song_popularity(self, saved_to_file=False):
        print('Top 5 Artists by average song popularity:')
        result_df = artist_rank_by_column(self.df, 'popularity').head(5)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/popularity', f'top_5_artists_by_average_song_popularity')

    def print_top_5_most_rated_song_per_artist(self, saved_to_file=False):
        print('Top 5 artists and their most popular song:')
        result_df = most_rated_song_per_artist_by_column(self.df, 'popularity').head(5)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/popularity', f'5_most_rated_song_per_artist')

    def print_top_5_most_rated_songs_in_year(self, year, saved_to_file=False):
        print(f'Top 5 most popular songs in the year {year}:')
        result_df = most_rated_in_year_by_column(self.df, year, 'popularity').head(5)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/popularity', f'top_5_most_rated_songs_in_year_{year}')

    def plot_most_popular_song_for_artist_in_every_year(self, artist_name, saved_to_file=False):
        print(f'The most popular song for {artist_name} in every year they released a song, graphed:')
        result_df = artist_most_column_song_rank_over_the_years(self.df, artist_name, 'popularity')
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/popularity', f'most_popular_song_for_{artist_name}_in_every_year')


# ---------------------------------------------------------------------------------------------------------------------------

class DataDanceability:
    def __init__(self, filename):
        self.filename = filename
        self.df = fix_data(load_data('songs_normalize.csv'))

    def plot_top_5_most_danceable_songs(self, saved_to_file=False):
        result_df = top_n_by_graph(self.df, 5, 'danceability')

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/danceability', f'top_5_most_danceable_songs')

    def print_artists_starting_with_letter(self, letter, saved_to_file=False):
        print(f'All artists in the DF that start with the letter {letter.upper()}')
        result_df = get_artists_starting_with_letter(self.df, letter)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/danceability', f'artists_starting_with_letter_{letter.upper()}')

    def print_average_song_danceability_of_artist(self, artist_name):
        print(f'The average song danceability of {artist_name} is:')
        result_df = average_rating_per_artist_by_column(self.df, artist_name, 'danceability').iloc[0][
            f'Avg_Songs_Rating_By_danceability']
        print(result_df)

    def print_top_5_most_danceable_songs_of_artist(self, artist_name, saved_to_file=False):
        print(f'The top 5 most danceable songs of {artist_name} are:')
        result_df = most_rated_song_for_artist_by_column(self.df, artist_name, 'danceability').head(5)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/danceability', f'top_5_most_danceable_songs_of_{artist_name}')

    def print_top_5_artists_by_average_song_danceability(self, saved_to_file=False):
        print('Top 5 Artists by average song danceability:')
        result_df = artist_rank_by_column(self.df, 'danceability').head(5)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/danceability', f'top_5_artists_by_average_song_danceability')

    def print_top_5_most_rated_song_per_artist(self, saved_to_file=False):
        print('Top 5 artists and their most danceable song:')
        result_df = most_rated_song_per_artist_by_column(self.df, 'danceability').head(5)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/danceability', f'5_most_rated_danceable_song_per_artist')

    def print_top_5_most_rated_danceable_songs_in_year(self, year, saved_to_file=False):
        print(f'Top 5 most danceable songs in the year {year}:')
        result_df = most_rated_in_year_by_column(self.df, year, 'danceability').head(5)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/danceability', f'top_5_most_rated_danceable_songs_in_year_{year}')

    def plot_most_danceable_song_for_artist_in_every_year(self, artist_name, saved_to_file=False):
        print(f'The most danceable song for {artist_name} in every year they released a song, graphed:')
        result_df = artist_most_column_song_rank_over_the_years(self.df, artist_name, 'danceability')
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/danceability', f'most_danceable_song_for_{artist_name}_in_every_year')


# ---------------------------------------------------------------------------------------------------------------------------

class DataEnergy:
    def __init__(self, filename):
        self.filename = filename
        self.df = fix_data(load_data('songs_normalize.csv'))

    def plot_top_5_most_energetic_songs(self, saved_to_file=False):
        result_df = top_n_by_graph(self.df, 5, 'energy')

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/energy', f'top_5_most_energetic_songs')

    def print_artists_starting_with_letter(self, letter, saved_to_file=False):
        print(f'All artists in the DF that start with the letter {letter.upper()}')
        result_df = get_artists_starting_with_letter(self.df, letter)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/energy', f'artists_starting_with_letter_{letter.upper()}')

    def print_average_song_energy_of_artist(self, artist_name):
        print(f'The average song energy of {artist_name} is:')
        result_df = average_rating_per_artist_by_column(self.df, artist_name, 'energy').iloc[0][
            f'Avg_Songs_Rating_By_energy']
        print(result_df)

    def print_top_5_most_energetic_songs_of_artist(self, artist_name, saved_to_file=False):
        print(f'The top 5 most energetic songs of {artist_name} are:')
        result_df = most_rated_song_for_artist_by_column(self.df, artist_name, 'energy').head(5)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/energy', f'top_5_most_energetic_songs_of_{artist_name}')

    def print_top_5_artists_by_average_song_energy(self, saved_to_file=False):
        print('Top 5 Artists by average song energy:')
        result_df = artist_rank_by_column(self.df, 'energy').head(5)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/energy', f'top_5_artists_by_average_song_energy')

    def print_top_5_most_rated_song_per_artist(self, saved_to_file=False):
        print('Top 5 artists and their most energetic song:')
        result_df = most_rated_song_per_artist_by_column(self.df, 'energy').head(5)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/energy', f'5_most_rated_energetic_song_per_artist')

    def print_top_5_most_rated_energetic_songs_in_year(self, year, saved_to_file=False):
        print(f'Top 5 most energetic songs in the year {year}:')
        result_df = most_rated_in_year_by_column(self.df, year, 'energy').head(5)
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/energy', f'top_5_most_rated_energetic_songs_in_year_{year}')

    def plot_most_energetic_song_for_artist_in_every_year(self, artist_name='Eminem', saved_to_file=False):
        print(f'The most energetic song for {artist_name} in every year they released a song, graphed:')
        result_df = artist_most_column_song_rank_over_the_years(self.df, artist_name, 'energy')
        print(result_df)

        if saved_to_file:
            save_df_to_csv(result_df, 'Saved_Files/energy', f'most_energetic_song_for_{artist_name}_in_every_year')
