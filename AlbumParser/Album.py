from AlbumParser.AlbumParsing import AlbumParsing
ALBUMS_TO_SHOW = 50  # can only display 50 albums at once (maximum)
ID = "id" # a relevant string for the album id


class Album:
    """
    this class represents an album in google photos. an album instance can be generated with a single input:
    the album's name
    """

    def __init__(self, service, title):
        """
        constructor for an album instance
        """
        self.all_albums = service.albums().list(pageSize=ALBUMS_TO_SHOW).execute() # TODO: maybe should be static
        self.service = service  # TODO: maybe should be static
        self.__title = title
        self.__album_data = AlbumParsing.get_album_by_title(title)
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

