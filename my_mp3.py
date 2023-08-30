while True:
    saved_songs = []
    file = "playlist1.txt"

    with open("playlist1.txt", 'r') as f:
        contents = f.read()

    print(
        "What would you like to do? \n 1. Load a playlist \n 2. Display all songs in a playlist \n 3. Add songs to a playlist \n 4. Remove songs from a playlist")
    request = int(input("Enter the either the number corresponding to your response: "))


    def load_songs():
        global contents


    def display_songs():
        print(contents)


    def add_songs():
        new_song = input("The title of the song: ")
        with open("playlist1.txt", 'a') as w:
            w.write("\n" + new_song)
        print("Song has been added successfully!")


    def remove_songs():
        global contents
        with open("playlist1.txt", 'r') as f:
            line = f.readline()
        num = int(input("How many songs are you removing: "))
        for x in range(num):
            delete = input("Song title: ")
            contents = contents.replace(delete,"")`
        with open(file, 'w') as t:
            t.write(contents)
        print("Track deleted")
        # for index in saved_songs:
        #     with open(file, 'a') as w:
        #         w.write('\n' + index)


    #      with open("playlist1.txt", 'a') as d:

    remove_songs()
    print(contents)
    # if request == 1:
    #     load_songs()
    # if request == 2:
    #     display_songs()
    # if request == 3:
    #     add_songs()
    # if request == 4:
    #     remove_songs()
