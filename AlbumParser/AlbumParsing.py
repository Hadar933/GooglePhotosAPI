"""
in this file we perform all the parsing that is relevant to an album. additing albums, iterating over albums, etc...
"""

from AlbumParser.DuplicateException import DuplicateException
from Initializer.InitializeData import create_service
from Main.InvalidInputException import InvalidInputException

ALBUMS_TO_SHOW = 50  # can only display 50 albums at once (maximum)

# MESSAGES: #
ALBUM_CREATION_SUCCESS_MSG = "AlbumParser {0} created successfully"
ALBUM_DUPLICATE_MSG = "AlbumParser {0} already exists. did not create album"
NO_ALBUM_MSG = "These isn't an album named: "

# RELEVANT STRINGS: #
TITLE = "title"

API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = '../client_Secret.json'
READ_WRITE_SCOPE = ['https://www.googleapis.com/auth/photoslibrary']
SHARE_SCOPE = ['https://www.googleapis.com/auth/photoslibrary.sharing']
SCOPES = [READ_WRITE_SCOPE, SHARE_SCOPE]

SERVICE = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
ALL_ALBUMS = SERVICE.albums().list(pageSize=ALBUMS_TO_SHOW).execute()


def get_albums_map():
    """
    getter for the response (the map containing the albums)
    """
    return ALL_ALBUMS.get("albums")


def doesAlbumExist(self, title):
    """
    checks if given album title is already in the data
    :param title: some albums name
    :return: true: exists, false: otherwise
    """
    for album in self.get_albums_map():
        if album.get(TITLE) == title:
            return True
    return False


def create_album(self, album_name):
    """
    creates an album with the given album name
    :param album_name: some string representing a wanted name
    :return: void
    """
    request_body = {"album": {"title": album_name}}
    if not self.doesAlbumExist(album_name):
        self.SERVICE.albums().create(body=request_body).execute()
        print(ALBUM_CREATION_SUCCESS_MSG.format(album_name))
    raise DuplicateException(ALBUM_DUPLICATE_MSG.format(album_name))


def get_album_by_title(self, title):
    """
    finds album with given title in the data, prints an error if album
    doesnt exist
    O(N) runtime (where N = number of albums, usually a rather small number)
    :param title: some albums name
    :return: album dictionary or failure error code
    """
    for album in self.get_albums_map():
        if album.get(TITLE) == title:
            return album
    raise InvalidInputException(NO_ALBUM_MSG + title)
