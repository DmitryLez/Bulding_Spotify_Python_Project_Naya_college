from data import load_data, fix_data
import pandas as pd
import matplotlib.pyplot as plt

# Adjust display settings to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = load_data()
df = pd.DataFrame(fix_data(df))

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


# Generate the graph for the top 10 songs by 'avg_score'
top_n_by_graph(df, 10, 'avg_score')

