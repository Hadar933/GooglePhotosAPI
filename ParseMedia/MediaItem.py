class MediaItem:
    """
    this class represents a video or an image
    """

    def __init__(self,service):
        """
        constructor
        """
        response = service.mediaItems().list(pageSize=25).execute()
