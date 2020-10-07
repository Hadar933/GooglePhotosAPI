class InvalidInputException(Exception):
    """
    this class is being called when theres a problem with the given input (ex. no album with given album name)
    """
    def __init__(self, msg):
        super().__init__(msg)
