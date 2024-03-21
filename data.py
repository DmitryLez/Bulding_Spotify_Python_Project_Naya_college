import pandas as pd

def load_data():
    # loading the data and cleaning the data and keeping only columns we need for the project.
    pd.set_option('display.max_columns', 24)
    df = pd.read_csv('songs_normalize.csv', encoding='latin1',
                     usecols=['artist', 'song', 'duration_ms', 'year', 'popularity', 'danceability', 'energy',
                              'genre'])

    return df


def fix_data(df):
    # Replace empty strings ('') and 'None' with NaN
    df.replace(['', 'None'], pd.NA, inplace=True)

    # Replace NaN values in 'popularity', 'danceability', and 'energy' columns with 0
    df['popularity'] = df['popularity'].fillna(0)
    # Convert 'danceability' column to numeric and fill NaN values with 0
    df['danceability'] = pd.to_numeric(df['danceability'], errors='coerce').fillna(0)
    # Convert 'energy' column to numeric and fill NaN values with 0
    df['energy'] = pd.to_numeric(df['energy'], errors='coerce').fillna(0)

    # Multiply 'danceability' and 'energy' by 100 and round to 2 decimal places
    df['danceability'] *= 100
    df['energy'] *= 100

    # Convert 'duration_ms' to duration in minutes and round to 2 decimal places
    df['duration_min'] = (df['duration_ms'] / (1000 * 60)).round(2)
    # Drop the original 'duration_ms' column
    df.drop(columns=['duration_ms'], inplace=True)

    # Round 'popularity', 'danceability', 'energy', and 'avg_score' to 2 decimal places
    df['popularity'] = df['popularity'].round(2)
    df['danceability'] = df['danceability'].round(2)
    df['energy'] = df['energy'].round(2)

    # Calculate the average of 'popularity', 'danceability', and 'energy' columns for each row
    df['avg_score'] = df[['popularity', 'danceability', 'energy']].mean(axis=1).round(2)

    # Check for nulls in artist name or song and remove them.
    df = df[df['artist'].notnull() & df['song'].notnull()]

    # Reset index
    df.reset_index(drop=True, inplace=True)

    return df







