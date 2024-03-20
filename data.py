import pandas as pd


def get_data():
    # loading the data and cleaning the data and keeping only columns we need for project.
    pd.set_option('display.max_columns', 24)
    df = pd.read_csv('songs_normalize.csv', encoding='latin1',
                     usecols=['artist', 'song', 'duration_ms', 'year', 'popularity', 'danceability', 'energy',
                              'genre'])

    # changing the name of duration_ms column to duration_minutes
    df.rename(columns={'duration_ms': 'duration_minutes'}, inplace=True)

    # Convert duration from milliseconds to minutes
    df['duration_minutes'] = df['duration_minutes'] / (1000 * 60)

    return df

def get_df_with_unqiue_artist_names():
    df = get_data()
    # Convert 'artist' column to lowercase and then get unique values
    unique_artists = df['artist'].unique()

    # Create a new DataFrame with unique values and indexes from 0
    unique_df = pd.DataFrame(unique_artists, columns=['artist'])

    # Sort the DataFrame alphabetically by the 'artist' column
    unique_df = unique_df.sort_values(by='artist')

    # Reset the index to start from 0
    unique_df = unique_df.reset_index(drop=True)

    return unique_df