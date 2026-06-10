class Song:
    """Representation of a song and global song registry.

    Responsibilities:
    - Instance attributes: `name`, `artist`, `genre`.
    - Class aggregates: `count`, `genres`, `artists`, `genre_count`, `artist_count`.
    """

    # Total number of Song instances created
    count = 0

    # Unique genres and artists seen across all Song instances
    genres = []
    artists = []

    # Maps used to count how many songs belong to each genre/artist
    genre_count = {}
    artist_count = {}

    # Alias requested by lab: `artists_count` should reference same map
    artists_count = artist_count

    # Keep references to all created Song instances
    all = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Register this instance in the global list
        Song.all.append(self)

        # Update class-level aggregates using helper methods
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
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
