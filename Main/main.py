"""
Google photos API can be found here:
https://developers.google.com/photos/library/reference/rest/v1/albums/batchRemoveMediaItems

to use this code, one must open an account (free) in google cloud platforms:
https://console.cloud.google.com

                        ~MAKE SURE YOU'VE READ THE README.md~
"""

# IMPORTS: #
from AlbumParser.Album import Album
import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# SERVICE DATA: #
API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = '../client_Secret.json'
READ_WRITE_SCOPE = ['https://www.googleapis.com/auth/photoslibrary']
SHARE_SCOPE = ['https://www.googleapis.com/auth/photoslibrary.sharing']
SCOPES = [READ_WRITE_SCOPE, SHARE_SCOPE]


def create_service(client_secret_file, api_name, api_version, scopes):
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



if __name__ == '__main__':
    service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    sri_lanka = Album(service, "Sri Lanka")
    print(sri_lanka)

    # media = MediaParser(service)
    # print(media.fetch_media_from_album(100))
