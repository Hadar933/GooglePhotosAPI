from AlbumParser.Album import Album

MEDIA_TO_SHOW = 100  # 100 is the maximum
MEDIA_ITEM_ID = "mediaItems"  # identifier for the media item to be requested
NEXT_TOKEN_ID = "nextPageToken"  # identifier for the media item to be requested
SUCCESS = 1
FAILURE = 0


class Media:
    """
    this class represents a video or an image
    """

    def __init__(self, service):
        """
        constructor for a media dictionary
        """
        self.__service = service
        self.__media = service.mediaItems().list(pageSize=MEDIA_TO_SHOW).execute()

    def getMedia(self):
        """
        getter for the media map
        """
        return self.__media

    def fetch_media_from_album(self, album_name):
        """
        returns a media item list that contains all elements (photos/videos)
        from the album named album_name
        """
        media_item_lst = []
        page_token = ""
        album = Album(self.__service).get_album_by_title(album_name)
        while True:
            body = {
                "albumId": Album(self.__service).__set_album_id(album),
                "pageToken": page_token if page_token != "" else ""

            }
            curr = self.__service.mediaItems().list(pageSize=MEDIA_TO_SHOW, pageToken=token).execute()
            media_items = curr.get(MEDIA_ITEM_ID, [])
            media_item_lst.extend(media_items)
            page_token = curr.get(NEXT_TOKEN_ID)
            if not page_token:
                break
            print("fetched ", len(media_item_lst), "/", n, "media items")
        return media_item_lst
