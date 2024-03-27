from data import *
from functions import *
import pandas as pd
from classes import *

# Adjust display settings to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print('--------------------------------------------Popularity---------------------------------------------------------')

songs = DataPopularity('songs_normalize.csv')
songs.print_artists_starting_with_letter('e', saved_to_file=True)
songs.print_average_song_popularity_of_artist('Eminem')
songs.print_top_5_most_popular_songs_of_artist('Eminem')
songs.print_top_5_artists_by_average_song_popularity()
songs.print_top_5_most_rated_song_per_artist()
songs.print_top_5_most_rated_songs_in_year(2007)
songs.plot_top_5_most_popular_songs()
songs.plot_most_popular_song_for_artist_in_every_year(artist_name='Eminem')

print('--------------------------------------------Danceability-------------------------------------------------------')

songs = DataDanceability('songs_normalize.csv')
songs.print_artists_starting_with_letter('b')  # Assuming you want artists starting with 'B'
songs.print_average_danceability_of_artist('Britney Spears')
songs.print_top_5_most_danceable_songs_of_artist('Britney Spears')
songs.print_top_5_artists_by_average_danceability()
songs.print_top_5_most_danceable_song_per_artist()
songs.print_top_5_most_danceable_songs_in_year(2007)
songs.plot_top_5_most_danceable_songs()
songs.plot_most_danceable_song_for_artist_in_every_year(artist_name='Britney Spears')

print('--------------------------------------------Energy-------------------------------------------------------------')

songs = DataEnergy('songs_normalize.csv')
songs.print_artists_starting_with_letter('r')
songs.print_average_energy_of_artist('Red Hot Chili Peppers')
songs.print_top_5_most_energetic_songs_of_artist('Red Hot Chili Peppers')
songs.print_top_5_artists_by_average_energy()
songs.print_top_5_most_energetic_song_per_artist()
songs.print_top_5_most_energetic_songs_in_year(2007)
songs.plot_top_5_most_energetic_songs()
songs.plot_most_energetic_song_for_artist_in_every_year(artist_name='Red Hot Chili Peppers')
