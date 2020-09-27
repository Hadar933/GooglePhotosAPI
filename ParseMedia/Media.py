MEDIA_TO_SHOW = 100  # 100 is the maximum


class Media:
    """
    this class represents a video or an image
    """

    def __init__(self, service):
        """
        constructor for a media dictionary
        """
        self.__media = service.mediaItems().list(pageSize=MEDIA_TO_SHOW).execute()

    def getMedia(self):
        return self.__media
