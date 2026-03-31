class playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []

    def add_song(self,song):
        self.songs.append(song)
        print(f"Added song: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed song: {song}")

    def show_songs(self):
        print(f"Playlist: {self.name}")
        for song in self.songs:
            print(f" - {song}")

myplaylist = playlist("Spotify Fav")
myplaylist.add_song("Bohemian Rapsody")
myplaylist.add_song("Wake me up when September ends")
myplaylist.add_song("All My Life")
myplaylist.add_song("Hotel California")
myplaylist.add_song("The Scientist")
myplaylist.add_song("Sparks")
myplaylist.remove_song("Sparks")
myplaylist.show_songs()