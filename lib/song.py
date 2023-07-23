class Song:
    genres=[]#empty list to track genre
    artists = []#empty list to track artist
    count = 0
    genre_count={}#dicitionary genre key: value of number of songs
    artist_count = {}#dicitionary artist key: value of number of songs

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        
    @classmethod
    def add_song_to_count(cls,increment = 1):
        cls.count +=increment
        
    @classmethod
    def add_to_genres(cls,genre):
        if cls.genres.count(genre) == 0:
            cls.genres.append(genre) # add genre to genreslist
            cls.genre_count[genre] = 1 # key genre : value song count
        else:
            cls.genre_count[genre] +=1  
    @classmethod
    def add_to_artists(cls,artist):
        if cls.artists.count(artist) == 0:
            cls.artists.append(artist) #add artist to artists list
            cls.artist_count[artist] = 1 #key artist: value song count
        else:
            cls.artist_count[artist] +=1

    @classmethod
    def add_to_genre_count(cls):
        return cls.genre_count

    @classmethod
    def add_to_artist_count(cls):
        return cls.artist_count

# Song("99 Problems", "Jay Z", "Rap")
# Song("Halo", "Beyonce", "Pop")
# Song("Smells Like Teen Spirit", "Nirvana", "Rock")
# Song("Hola", "Nirvana", "Pop")
# Song("Smells Like Teen Spirit", "Nirvana", "Rap")
# Song("happy birthday","danny","Hiphop")
# print(Song.count)
# print(Song.genres)
# print(Song.artists)
# print(Song.genre_count)
# print(Song.artist_count)
