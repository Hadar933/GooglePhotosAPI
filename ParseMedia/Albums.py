# IMPORTS: #
from Init.Initializer import create_service

# RELEVANT CONSTANTS: #
ALBUMS_TO_SHOW = 50  # can only display 50 albums at once (maximum)
SUCCESS = 1
FAILURE = 0

# MESSAGES: #
NO_ALBUM_MSG = "These isn't an album named: "
NON_EXISTING_MSG = "album {0} doesnt exist."
ALBUM_CREATION_SUCCESS_MSG = "Album {0} created successfully"
ALBUM_DUPLICATE_MSG = "Album {0} already exists. did not create album"
ALBUM_CREATION_FAIL_MSG = "Could not create album "

# RELEVANT STRINGS: #
TITLE = "title"
ID = "id"
ALBUMS = "albums"


class Albums:
    """
    this class represents the albums in google photos
    """

    def __init__(self, service):
        """
        constructor for albums dictionary
        """
        self.__albums = service.albums().list(pageSize=ALBUMS_TO_SHOW).execute().get(ALBUMS)  # map of albums

    def get_albums_map(self):
        """
        getter for the response (the map containing the albums)
        """
        return self.__albums

    def get_album_by_title(self, title):
        """
        finds album with given title in the data, prints an error if album
        doesnt exist
        :param title: some albums name
        :return: album dictionary or failure error code
        """
        for album in self.__albums:
            if album.get(TITLE) == title:
                return album
        print(NO_ALBUM_MSG + title)
        return FAILURE

    def doesAlbumExist(self, title):
        """
        checks if given album title is already in the data
        :param title: some albums name
        :return: true: exists, false: otherwise
        """
        for album in self.__albums:
            if album.get(TITLE) == title:
                return True
        return False

    def get_album_title(self, album):
        """
        returns the name of the given album
        :param album: some album dictionary
        :return: name of the album (string)
        """
        try:
            title = album.get(TITLE)
        except AttributeError:
            print(NON_EXISTING_MSG.format(album))
            return FAILURE
        return title

    def get_album_id(self, album):
        """
        returns the id of the given album
        :param album: some album dictionary
        :return: id of the album (string)
        """
        try:
            id = album.get(ID)
        except AttributeError:
            print(NON_EXISTING_MSG.format(album))
            return FAILURE
        return id

    def create_album(self, album_name):
        """
        creates an album with the given album name
        :param album_name: some string representing a wanted name
        :return: void
        """
        request_body = {"album": {"title": album_name}}
        if not self.doesAlbumExist(album_name):
            self.__albums.create(body=request_body).execute()
            print(ALBUM_CREATION_SUCCESS_MSG.format(album_name))
            return SUCCESS
        print(ALBUM_DUPLICATE_MSG.format(album_name))
        return FAILURE
