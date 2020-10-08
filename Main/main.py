"""
Google photos API can be found here:
https://developers.google.com/photos/library/reference/rest/v1/albums/batchRemoveMediaItems

to use this code, one must open an account (free) in google cloud platforms:
https://console.cloud.google.com

                        ~MAKE SURE YOU'VE READ THE README.md~
"""
from AlbumParser import AlbumParsing as ap

if __name__ == '__main__':

    for item in ap.find_media_based_on_filter(["SPORT"], True):
        print(item)
