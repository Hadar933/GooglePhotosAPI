MEDIA_TO_SHOW = 100  # 100 is the maximum
MEDIA_ITEM_ID = "mediaItems"  # identifier for the media item to be requested
NEXT_TOKEN_ID = "nextPageToken"  # identifier for the media item to be requested


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

    def fetch_n_items(self, n):
        """
        returns a media item list that contains n elements (photos/videos)
        n is an estimate, there might be a little more items in the final array (since were adding in bulks)
        """
        media_item_lst = []
        page_token = ""
        while len(media_item_lst) < n:
            token = page_token if page_token != "" else ""
            curr = self.__service.mediaItems().list(pageSize=MEDIA_TO_SHOW, pageToken=token).execute()
            media_items = curr.get(MEDIA_ITEM_ID, [])
            media_item_lst.extend(media_items)
            page_token = curr.get(NEXT_TOKEN_ID)
            if not page_token:
                break
            print("added ", len(media_item_lst), "/", n, "media items")
        return media_item_lst
