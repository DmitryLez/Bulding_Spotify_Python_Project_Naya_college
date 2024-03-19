import pandas as pd
pd.set_option('display.max_columns', 24)
df = pd.read_csv('spotify-2023.csv', encoding='latin1') #loading the data
columns_to_keep = ['track_name', 'artist(s)_name', 'released_year','in_spotify_playlists','streams']

print(df.head(1))
print(df.shape)