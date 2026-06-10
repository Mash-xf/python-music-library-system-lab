class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    # backward- and forward-compatible naming
    artists_count = artist_count

    all = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.all.append(self)

        # use class methods for each update so external callers can use them too
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artists_count(self.artist)

    @classmethod
    def all_songs(cls):
        return list(cls.all)

    @classmethod
    def add_song(cls, name, artist, genre):
        return cls(name, artist, genre)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        # keep both `artist_count` and `artists_count` in sync (they are the same object)
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
