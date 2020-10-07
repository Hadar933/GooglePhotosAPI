class DuplicateException(Exception):
    """
    this class is being called when the user wishes to add a new album, but
    theres already an album with the same name in the data
    """
    def __init__(self, msg):
        super().__init__(msg)
