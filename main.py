from data import *
from functions import *
import pandas as pd
from classes import *

# Adjust display settings to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print('--------------------------------------------Popularity---------------------------------------------------------')

# For Popularity
songs = DataPopularity('songs_normalize.csv')
songs.print_artists_starting_with_letter('e', saved_to_file=True)
songs.print_average_song_popularity_of_artist('Eminem')
songs.print_top_5_most_popular_songs_of_artist('Eminem', saved_to_file=True)
songs.print_top_5_artists_by_average_song_popularity(saved_to_file=True)
songs.print_top_5_most_rated_song_per_artist(saved_to_file=True)
songs.print_top_5_most_rated_songs_in_year(2007, saved_to_file=True)
songs.plot_top_5_most_popular_songs(saved_to_file=True)
songs.plot_most_popular_song_for_artist_in_every_year(artist_name='Eminem', saved_to_file=True)

print('--------------------------------------------Danceability-------------------------------------------------------')

# For Danceability
songs_dance = DataDanceability('songs_normalize.csv')
songs_dance.print_artists_starting_with_letter('b', saved_to_file=True)
songs_dance.print_average_song_danceability_of_artist('Britney Spears')
songs_dance.print_top_5_most_danceable_songs_of_artist('Britney Spears', saved_to_file=True)
songs_dance.print_top_5_artists_by_average_song_danceability(saved_to_file=True)
songs_dance.print_top_5_most_rated_song_per_artist(saved_to_file=True)
songs_dance.print_top_5_most_rated_danceable_songs_in_year(2007, saved_to_file=True)
songs_dance.plot_top_5_most_danceable_songs(saved_to_file=True)
songs_dance.plot_most_danceable_song_for_artist_in_every_year(artist_name='Britney Spears', saved_to_file=True)

print('--------------------------------------------Energy-------------------------------------------------------------')

# For Energy
songs_energy = DataEnergy('songs_normalize.csv')
songs_energy.print_artists_starting_with_letter('r', saved_to_file=True)
songs_energy.print_average_song_energy_of_artist('Red Hot Chili Peppers')
songs_energy.print_top_5_most_energetic_songs_of_artist('Red Hot Chili Peppers', saved_to_file=True)
songs_energy.print_top_5_artists_by_average_song_energy(saved_to_file=True)
songs_energy.print_top_5_most_rated_song_per_artist(saved_to_file=True)
songs_energy.print_top_5_most_rated_energetic_songs_in_year(2007, saved_to_file=True)
songs_energy.plot_top_5_most_energetic_songs(saved_to_file=True)
songs_energy.plot_most_energetic_song_for_artist_in_every_year(artist_name='Red Hot Chili Peppers', saved_to_file=True)
