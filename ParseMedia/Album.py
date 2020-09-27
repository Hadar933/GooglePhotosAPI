"""
Google photos API can be found here:
https://developers.google.com/photos/library/reference/rest/v1/albums/batchRemoveMediaItems

to use this code, one must open an account (free) in google cloud platforms:
https://console.cloud.google.com
"""

# IMPORTS: #
import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# SERVICE DATA: #
API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = '../Client_Secret.json'
READ_WRITE_SCOPE = 'https://www.googleapis.com/auth/photoslibrary'
SHARE_SCOPE = 'https://www.googleapis.com/auth/photoslibrary.sharing'
SCOPES = [READ_WRITE_SCOPE, SHARE_SCOPE]

# RELEVANT CONSTANTS: #
ALBUMS_TO_SHOW = 50  # can only display 50 albums at once (maximum)
SUCCESS = 1
FAILURE = 0

# RELEVANT STRINGS: #
NO_ALBUM_MSG = "These isn't an album named: "
NON_EXISTING_MSG = "album {0} doesnt exist."
ALBUM_CREATION_SUCCESS_MSG = "Album {0} created successfully"
ALBUM_DUPLICATE_MSG = "Album {0} already exists. did not create album"
ALBUM_CREATION_FAIL_MSG = "Could not create album "

TITLE = "title"
ID = "id"
ALBUMS = "albums"


def Album(client_secret_file, api_name, api_version, scopes):
    """
    a static method that generates a service to work on from given data
    this specific function was written by Jie Jenn (youtube)
    :param client_secret_file: provided secret file info from google
    :param api_name: name of the api
    :param api_version: version of the api
    :param scopes: the scopes to which we need access
    :return: the service, or null
    """
    print(client_secret_file, api_name, api_version, scopes, sep=', ')
    SCOPES = [scope for scope in scopes[0]]
    cred = None
    pickle_file = f'token_{api_name}_{api_version}.pickle'
    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secret_file, SCOPES)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    service = build(api_name, api_version, credentials=cred)
    print(api_name, 'service created successfully')
    return service


class Parser:
    """
    this class performs various operations on the server
    """

    def __init__(self):
        """
        constructor
        """
        self.__service = Album(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        self.__response = self.__service.albums().list(pageSize=ALBUMS_TO_SHOW).execute()  # a map of all the media
        self.__albums = self.__response.get(ALBUMS)  # a map of albums

    def get_albums_map(self):
        """
        getter for the response (the map containing the albums)
        """
        return self.__albums

    def get_album_by_title(self, title):
        """
        finds album with given title in the data, prints an error if album
        doesnt exist
        :param title: some albums name
        :return: album dictionary
        """
        for album in self.__albums:
            if album.get(TITLE) == title:
                return album
        print(NO_ALBUM_MSG + title)

    def doesAlbumExist(self, title):
        """
        checks if given album title is already in the data
        :param title: some albums name
        :return: true: exists, false: otherwise
        """
        for album in self.__albums:
            if album.get(TITLE) == title:
                return True
        return False

    def get_album_title(self, album):
        """
        returns the name of the given album
        :param album: some album dictionary
        :return: name of the album (string)
        """
        try:
            title = album.get(TITLE)
        except AttributeError:
            print(NON_EXISTING_MSG.format(album))
            return FAILURE
        return title

    def get_album_id(self, album):
        """
        returns the id of the given album
        :param album: some album dictionary
        :return: id of the album (string)
        """
        try:
            id = album.get(ID)
        except AttributeError:
            print(NON_EXISTING_MSG.format(album))
            return FAILURE
        return id

    def create_album(self, album_name):
        """
        creates an album with the given album name
        :param album_name: some string representing a wanted name
        :return: void
        """
        request_body = {"album": {"title": album_name}}
        if not self.doesAlbumExist(album_name):
            self.__service.albums().create(body=request_body).execute()
            print(ALBUM_CREATION_SUCCESS_MSG.format(album_name))
            return SUCCESS
        print(ALBUM_DUPLICATE_MSG.format(album_name))
        return FAILURE

    def add_item_to_album(self, album_title):
        album = self.get_album_by_title(album_title)
        id = album.get(ID)


if __name__ == '__main__':
    p = Parser()
    title = "Sri Lanka"
    album = p.get_album_by_title(title)
    print(album.get(ID))
