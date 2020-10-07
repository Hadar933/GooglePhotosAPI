from AlbumParser import AlbumParsing


class Album:
    """
    this class represents an album in google photos. an album instance can be generated with a single input:
    the album's name
    """

    def __init__(self, media_id, title, product_url, media_items_count, cover_photos_base_url, cover_photo_id):
        """
        constructor for an album instance
        """
        self.__id = media_id
        self.__title = title
        self.__product_url = product_url
        self.__media_items_count = media_items_count
        self.__cover_photos_base_url = cover_photos_base_url
        self.__cover_photo_id = cover_photo_id

    def __str__(self):
        """
        :return: a string representation of the album
        """
        return "Album: " + str(self.__title) + "\n" + \
               "id = " + str(self.__id) + "\n" + \
               "product url = " + str(self.__product_url) + "\n" + \
               "media item count = " + str(self.__media_items_count) + "\n" + \
               "cover photo url = " + str(self.__cover_photos_base_url) + "\n" + \
               "cover photo id = " + str(self.__cover_photo_id) + "\n\n"

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_product_url(self):
        return self.__product_url

    def get_item_count(self):
        return self.__media_items_count

    def get_cover_photo_url(self):
        return self.__cover_photos_base_url

    def get_cover_id(self):
        return self.__cover_photo_id
