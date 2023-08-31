class Playlist:
    import random


    def __init__(self, ):
        self.loaded_songs = []

    def load_songs(self, file):
        with open(file, "r") as f:
            contents = f.readlines()
            self.loaded_songs = [line.strip() for line in contents]
            print("All done!")

    def display_songs(self):
        for song in self.loaded_songs:
            print(song)

    def add_songs(self, new_song):
        self.loaded_songs.append(new_song)
        with open("playlist1.txt", "a") as f:
            f.write(new_song + "\n")
        print("Song added successfully!")

    def remove_songs(self, song_to_remove):
        self.loaded_songs.remove(song_to_remove)

    def shuffle_playlist(self):
        random.shuffle(self.loaded_songs)


my_playlist = Playlist()
print(
    "What would you like to do? \n 0. Exit the system \n 1. Load a playlist \n 2. Display all songs in a playlist "
    "\n 3. Add songs to a playlist \n 4. Remove songs from a playlist \n 5. Shuffle playlist \n "
    "6. Count the songs in playlist \n 7. Clear playlist \n 8. Check if playlist is empty")

close = False

while not close:

    option = int(input("Enter the number corresponding to your response: "))

    if option == 0:
        print("exiting the system")
        close = True
    elif option == 1:
        my_playlist.load_songs("playlist1.txt")
    elif option == 2:
        my_playlist.display_songs()
    elif option == 3:
        new_song = input("Add new song: ")
        my_playlist.add_songs(new_song)
    elif option == 4:
        song_to_remove = input("Enter song to remove: ")
        my_playlist.remove_songs(song_to_remove)

