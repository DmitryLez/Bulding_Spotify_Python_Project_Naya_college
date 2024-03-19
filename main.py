import pandas as pd
from data import get_data
from classes import Song, Artist

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
for song in artists_array[0].songs:
    print(song)
