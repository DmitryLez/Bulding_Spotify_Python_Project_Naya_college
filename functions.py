import pandas as pd
import matplotlib.pyplot as plt


def top_n_by_graph(df, n, column):
    df_top_n = df.nlargest(n, column)
    df_top_n = df_top_n.loc[:, ['artist', 'song', column]]
    df_top_n.reset_index(drop=True, inplace=True)

    # Sort DataFrame by the specified column in ascending order
    df_top_n = df_top_n.sort_values(by=column, ascending=True)

    # Plotting the bar graph vertically
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(df_top_n['artist'] + ' - ' + df_top_n['song'], df_top_n[column], color='skyblue')
    ax.set_xlabel(column)
    ax.set_ylabel('Artist - Song')
    ax.set_title(f'Top {n} Songs by {column}')

    # Rotate tick labels on y-axis
    plt.yticks(rotation=45, ha='right')

    # Add value labels to the bars
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width:.2f}', va='center', ha='left')

    plt.tight_layout()
    plt.show()


def average_rating_per_artist_by_column(df, artist, column):
    # Filter df by artist name
    df_artist = df[df['artist'] == artist]

    # Calculate the average rating for the specified column
    avg_rating = df_artist[column].mean().round(2)

    # Create a new DataFrame with just one row
    result_df = pd.DataFrame({'artist': [artist], f'Avg_Songs_Rating_By_{column}': [avg_rating]})

    return result_df


def artist_rank_by_column(df, column):
    # Initialize an empty list to store the result DataFrames
    result_dfs = []

    # Iterate through each unique artist in the DataFrame
    for artist in df['artist'].unique():
        # Calculate the average rating for the specified column using avg_per_artist function
        avg_df = average_rating_per_artist_by_column(df, artist, column)

        # Append the resulting DataFrame to the list
        result_dfs.append(avg_df)

    # Concatenate all the result DataFrames into one DataFrame
    final_df = pd.concat(result_dfs, ignore_index=True)

    # Sort the final DataFrame by the specified column in descending order
    final_df = final_df.sort_values(by=f'Avg_Songs_Rating_By_{column}', ascending=False)

    # Reset index
    final_df.reset_index(drop=True, inplace=True)

    return final_df


def most_rated_song_for_artist_by_column(df, artist, column):
    # Filter df by artist name
    filtered_by_artist_df = pd.DataFrame(df[df['artist'] == artist])

    # Sort the filtered DataFrame by the specified column in descending order
    sorted_df = filtered_by_artist_df.sort_values(by=column, ascending=False)

    # Select specific columns for the sorted DataFrame using .loc[]
    needed_column_df = sorted_df.loc[:, ['artist', 'song', column]]

    # Reset index
    needed_column_df.reset_index(drop=True, inplace=True)
    return needed_column_df


def most_rated_song_per_artist_by_column(df, column):
    # Initialize an empty list to store the result DataFrames
    result_dfs = []

    # Iterate through each unique artist in the DataFrame
    for artist in df['artist'].unique():
        # Calculate the most rated by specified column using most_column_song_for_artist function
        most_rated_son_df = most_rated_song_for_artist_by_column(df, artist, column).head(1)

        # Append the resulting DataFrame to the list
        result_dfs.append(most_rated_son_df)

    # Concatenate all the result DataFrames into one DataFrame
    final_df = pd.concat(result_dfs, ignore_index=True)

    # Sort the final DataFrame by the specified column in descending order
    final_df = final_df.sort_values(by=column, ascending=False)

    # Reset index
    final_df.reset_index(drop=True, inplace=True)

    return final_df
