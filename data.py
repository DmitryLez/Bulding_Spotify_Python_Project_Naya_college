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
