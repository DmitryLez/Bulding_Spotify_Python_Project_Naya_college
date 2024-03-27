The primary goal of the project is to work with files and the Python Pandas library. 
Additionally, I endeavored to keep the project as modular as possible, allowing for easy expansion in the future with additional files and functionality.

it order  to showcase the project I have "Top Hits Spotify from 2000-2019" dataset I downloaded from kaggle.com.
![image](https://github.com/DmitryLez/Bulding_Spotify_Python_Project_Naya_college/assets/89594563/535c025e-e9d3-4069-bef3-9688b72d676d)


`data.py`: 
This file contains a `load_data` function, which loads 
the data based on the provided filename and returns it as a DataFrame.
![image](https://github.com/DmitryLez/Bulding_Spotify_Python_Project_Naya_college/assets/89594563/39785701-d2a1-4c6f-8de0-6dfc182a9564)

Next, there is a function named `fix_data`. This function organizes the provided DataFrame by removing unnecessary rows and columns, 
as well as filling in nulls, NAs, and empty rows. Additionally, it standardizes numeric values within the data. 
For example, some columns may contain percentages represented as integers (e.g., 87), while others may use double values (e.g., 0.87). 
This function ensures uniform formatting by converting all numeric values to the same percentage format.
![image](https://github.com/DmitryLez/Bulding_Spotify_Python_Project_Naya_college/assets/89594563/f0383368-99f7-439f-be30-24923f132c3f)


`test.py`:
This file was created to test the `fix_data` function and verify that it performs all the necessary steps to clean the data and prepare it for analysis.
It contains two dictionaries that are converted to DataFrames: "data" and "data_expected_after_fix". The `fix_data` function is applied to the "data" DataFrame, and the result is compared to the "data_expected_after_fix" DataFrame.
![image](https://github.com/DmitryLez/Bulding_Spotify_Python_Project_Naya_college/assets/89594563/c0b7571f-55c6-4c5b-a9fb-0c6d82b0a946)


`functions.py`:
This file contains all the functions that are used in the `classes.py` file later on. I aimed to make the functions as generic as possible to enable their use across many different classes with various columns.
For example, the function `top_n_by_graph(df, n, column)` is utilized to generate both a graph and a DataFrame. 
It filters the top entries based on the specified column, such as the "popularity" column, and returns a DataFrame containing the top n rows. Additionally, it prints a graph that visualizes the top n entries.
![image](https://github.com/DmitryLez/Bulding_Spotify_Python_Project_Naya_college/assets/89594563/8f912d27-f45d-472f-a324-1d22c8ecbfad)

`classes.py`:
This file contains three similar classes: `DataPopularity`, `DataDanceability`, and `DataEnergy`. They are separated into three classes to enhance the user experience when using the functions from the `functions.py` file.
For simplicity of usage, each class accepts only the CSV file name to be loaded, automatically loads it, fixes it, and facilitates the extraction of data into DataFrames and plots.
Additionally, every function that returns a DataFrame can be used together with the `saved_to_file=True` parameter to save the data into a named CSV file on the local machine.
![image](https://github.com/DmitryLez/Bulding_Spotify_Python_Project_Naya_college/assets/89594563/9a9e1a5f-c950-4056-8971-2019b5b9e43f)

`main.py`:
This file is primarily used to showcase the functionality of the classes in the clearest way possible. Each class has its own showcase. Here's an example showcasing the DataPopularity class:

First, we load the file into the class:
`songs = DataPopularity('songs_normalize.csv')`
Given that the CSV file is quite large and contains over 800 different artists, I decided that it would be easier to search for the required artist
by the first letter of its name instead of showcasing the entire list. Therefore, we can output both to a file and to the console window the artists that start with a certain letter, for example, 'e':
`songs.print_artists_starting_with_letter('e', saved_to_file=True)`
This approach enhances usability and simplifies the process of finding specific artists within the dataset.

The showcase includes several other functions, some of which are artist-specific and others that operate on the entire dataset. For example:
`songs.print_top_5_most_popular_songs_of_artist('Eminem', saved_to_file=True)`
`songs.print_top_5_artists_by_average_song_popularity(saved_to_file=True)`

Additionally, there are functions that both return a DataFrame and print it to the console, while also creating a file upon request and generating a plot. 
For instance, consider the following function, which plots Eminem's most popular song popularity over the past 19 years:
`songs.plot_most_popular_song_for_artist_in_every_year(artist_name='Eminem', saved_to_file=True)`
![image](https://github.com/DmitryLez/Bulding_Spotify_Python_Project_Naya_college/assets/89594563/b77cfee5-bb44-4a50-8b8f-a63ac560b24a)

![image](https://github.com/DmitryLez/Bulding_Spotify_Python_Project_Naya_college/assets/89594563/ec4d71f3-cc28-4789-9330-de5a61ea43fd)

![image](https://github.com/DmitryLez/Bulding_Spotify_Python_Project_Naya_college/assets/89594563/446963ac-4e57-46e6-8a44-676e58a9a9e7)


