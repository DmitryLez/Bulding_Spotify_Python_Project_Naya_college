import matplotlib.pyplot as plt


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

    import matplotlib.pyplot as plt

    def print_popularity_plot(self):
        sorted_song_by_popularity = sorted(self.songs, key=lambda x: float(x.popularity))
        songs_names = []
        songs_popularity = []
        for song in sorted_song_by_popularity:
            songs_names.append(song.name)
            songs_popularity.append(song.popularity)

        # Increase the figure size to avoid overlapping bars
        plt.figure(figsize=(10, 6))

        # Plotting the graph with adjusted bar width and spacing
        plt.bar(songs_names, songs_popularity, color='skyblue', width=0.5, align='center')

        # Adding labels and title
        plt.xlabel('Song Name')
        plt.ylabel('Popularity')
        plt.title(f'{self.name} Songs Popularity')

        # Set the y-axis limits to 0 and 100
        plt.ylim(0, 100)

        # Rotating x-axis labels for better readability
        plt.xticks(rotation=45, ha='right')

        # Displaying the graph
        plt.tight_layout()  # Adjust layout to prevent clipping of labels
        plt.show()

    def sort_array(self):
        return sorted(self.songs, key=lambda x: x.popularity)