import pandas as pd


class Song:
    def __init__(self, name, duration_minutes, year, popularity, danceability, energy, genre):
        self.name = name
        self.year = year
        self.popularity = popularity
        self.danceability = danceability
        self.energy = energy
        self.energy = genre


class Artist:
    def __init__(self, name):
        self.name = name


pd.set_option('display.max_columns', 24)
df = pd.read_csv('songs_normalize.csv', encoding='latin1')  # loading the data

df.rename(columns={'duration_ms': 'duration_minutes'}, inplace=True)

# # Convert duration from milliseconds to minutes
df['duration_minutes'] = df['duration_minutes'] / (1000 * 60)

columns_to_keep = ['artist', 'song', 'duration_minutes', 'year', 'popularity', 'danceability', 'energy',
                   'genre']  # cleaning the data and keeping only columns we need for project.
df = df[columns_to_keep]

print(df.head(1))
print(df.shape)
print(len(df['artist'].unique().tolist()))
