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