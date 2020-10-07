"""
Google photos API can be found here:
https://developers.google.com/photos/library/reference/rest/v1/albums/batchRemoveMediaItems

to use this code, one must open an account (free) in google cloud platforms:
https://console.cloud.google.com

                        ~MAKE SURE YOU'VE READ THE README.md~
"""
from AlbumParser import AlbumParsing as ap

if __name__ == '__main__':
    # mamek = ap.instantiate_album("fun with mamek")
    # for item in mamek.get_media():
    #     print(item)
    ap.download_album_content("fun with mamek")
