from data import get_data
from classes import Song, Artist
import tkinter as tk

df = get_data()
artists_array = []

for artist_name in (df['artist'].unique().tolist()):
    artists_array.append(Artist(artist_name))


for artist in artists_array:
    for index, row in df[df['artist'] == artist.name].iterrows():
        # Access row values using row['column_name']
        artist.songs.append(
            Song(row['song'], row['duration_minutes'], row['year'], row['popularity'], row['danceability'],
                 row['energy'], row['genre']))

# Printing songs for the first artist in the artists_array
# print(len(artists_array[6].songs))
# artists_array[54].print_popularity_plot()
#
#
#
# for song in artists_array[54].sort_array():
#     print(song)
#

# for song in artists_array[6].songs:
#     print(song)


# user ui
print('Hello Welcome to the Top Hits Spotify from 2000-2019 Project by Dmitry Lezinsky')

print('Please choose an artist from the following list: ')
print(artists_array)
