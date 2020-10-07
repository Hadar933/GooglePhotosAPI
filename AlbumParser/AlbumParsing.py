from AlbumParser.DuplicateException import DuplicateException

ALBUMS_TO_SHOW = 50  # can only display 50 albums at once (maximum)
SUCCESS = 1
FAILURE = 0

# MESSAGES: #
ALBUM_CREATION_SUCCESS_MSG = "AlbumParser {0} created successfully"
ALBUM_DUPLICATE_MSG = "AlbumParser {0} already exists. did not create album"

# RELEVANT STRINGS: #
TITLE = "title"


class AlbumParsing:
    def __init__(self, service):
        """
        constructor for an album parser
        """
        self.all_albums = service.albums().list(pageSize=ALBUMS_TO_SHOW).execute()  # TODO: maybe should be static
        self.service = service  # TODO: maybe should be static

    def get_albums_map(self):
        """
        getter for the response (the map containing the albums)
        """
        return self.all_albums.get("albums")

    def doesAlbumExist(self, title):
        """
        checks if given album title is already in the data
        :param title: some albums name
        :return: true: exists, false: otherwise
        """
        for album in self.get_albums_map():
            if album.get(TITLE) == title:
                return True
        return False

    def create_album(self, album_name):
        """
        creates an album with the given album name
        :param album_name: some string representing a wanted name
        :return: void
        """
        request_body = {"album": {"title": album_name}}
        if not self.doesAlbumExist(album_name):
            self.service.albums().create(body=request_body).execute()
            print(ALBUM_CREATION_SUCCESS_MSG.format(album_name))
        raise DuplicateException(ALBUM_DUPLICATE_MSG.format(album_name))
