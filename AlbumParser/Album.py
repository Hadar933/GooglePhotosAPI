# RELEVANT CONSTANTS: #
from Main.InvalidInputException import InvalidInputException

ALBUMS_TO_SHOW = 50  # can only display 50 albums at once (maximum)
SUCCESS = 1
FAILURE = 0

# MESSAGES: #
NO_ALBUM_MSG = "These isn't an album named: "
NON_EXISTING_MSG = "album {0} doesnt exist."
ALBUM_CREATION_SUCCESS_MSG = "AlbumParser {0} created successfully"
ALBUM_DUPLICATE_MSG = "AlbumParser {0} already exists. did not create album"
ALBUM_CREATION_FAIL_MSG = "Could not create album "

# RELEVANT STRINGS: #
TITLE = "title"
ID = "id"
ALBUMS = "albums"


class Album:
    """
    this class represents an album in google photos
    """

    def __init__(self, service, title):
        """
        constructor for an album instance
        """
        self.all_albums = service.albums().list(pageSize=ALBUMS_TO_SHOW).execute() # TODO: maybe should be static
        self.service = service  # TODO: maybe should be static
        self.__title = title
        self.__album_data = self.get_album_by_title()
        self.__id = self.__album_data.get(ID)

    def __str__(self):
        """
        a displayable representation of the album (called when printed)
        :return: a string that represents all the data of some album instance
        """
        output_str = "AlbumParser " + self.__title + "\n"
        for key in self.__album_data:
            output_str += key + ':' + self.__album_data[key] + "\n"
        return output_str

    def get_albums_map(self):
        """
        getter for the response (the map containing the albums)
        """
        return self.all_albums.get("albums")

    def doesAlbumExist(self):
        """
        checks if given album title is already in the data
        :param title: some albums name
        :return: true: exists, false: otherwise
        """
        for album in self.get_albums_map():
            if album.get(TITLE) == self.__title:
                return True
        return False

    def get_album_title(self):
        """
        returns the name of the given album
        :param album: some album dictionary
        :return: name of the album (string)
        """
        return self.__title

    def get_album_id(self):
        """
        getter for the album id
        """
        return self.__id

    def get_album_by_title(self):
        """
        finds album with given title in the data, prints an error if album
        doesnt exist
        :param title: some albums name
        :return: album dictionary or failure error code
        """
        for album in self.get_albums_map():
            if album.get(TITLE) == self.__title:
                return album
        raise InvalidInputException(NO_ALBUM_MSG + self.__title)

