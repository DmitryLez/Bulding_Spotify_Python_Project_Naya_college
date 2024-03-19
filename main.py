import pandas as pd
from Data import get_data


class Song:
    def __init__(self, name, duration_minutes, year, popularity, danceability, energy, genre):
        self.name = name
        self.duration_minutes = duration_minutes
        self.year = year
        self.popularity = popularity
        self.danceability = danceability
        self.energy = energy
        self.genre = genre

    def __str__(self):
        return f"Name: {self.name}, Duration: {self.duration_minutes} minutes, Year: {self.year}, Popularity: {self.popularity}, Danceability: {self.danceability}, Energy: {self.energy}, Genre: {self.genre}"


class Artist:
    def __init__(self, name):
        self.name = name
        self.songs = []


df = get_data()

artists_array = []
for artist_name in (df['artist'].unique().tolist()):
    artists_array.append(Artist(artist_name))

# for artist in artists_array:
#     print(artist.name)
# print('--------------------------------------')

for artist in artists_array:
    for index, row in df[df['artist'] == artist.name].iterrows():
        # Access row values using row['column_name']
        artist.songs.append(
            Song(row['song'], row['duration_minutes'], row['year'], row['popularity'], row['danceability'],
                 row['energy'], row['genre']))

# Printing songs for the first artist in the artists_array
for song in artists_array[0].songs:
    print(song)
