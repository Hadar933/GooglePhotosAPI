"""
Google photos API can be found here:
https://developers.google.com/photos/library/reference/rest/v1/albums/batchRemoveMediaItems

to use this code, one must open an account (free) in google cloud platforms:
https://console.cloud.google.com

                        ~MAKE SURE YOU'VE READ THE README.md~
"""

from Init.Initializer import create_service
from ParseMedia.Albums import Albums


# SERVICE DATA: #
API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = '../client_Secret.json'
READ_WRITE_SCOPE = ['https://www.googleapis.com/auth/photoslibrary']
SHARE_SCOPE = ['https://www.googleapis.com/auth/photoslibrary.sharing']
SCOPES = [READ_WRITE_SCOPE, SHARE_SCOPE]

if __name__ == '__main__':
    service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    a = Albums(service)
    title = "Sri Lanka"
    album = a.get_album_by_title(title)
    print(album.get("id"))
