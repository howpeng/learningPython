class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["happy birthday to you",
                   "I dont't want to get sued",
                   "so I'll love forever."])

happy_bday.sing_me_a_song()