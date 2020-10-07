"""
Google photos API can be found here:
https://developers.google.com/photos/library/reference/rest/v1/albums/batchRemoveMediaItems

to use this code, one must open an account (free) in google cloud platforms:
https://console.cloud.google.com

                        ~MAKE SURE YOU'VE READ THE README.md~
"""
import AlbumParser.AlbumParsing as ap

if __name__ == '__main__':
    d = ap.get_all_albums()
    for item in d:
        print(d[item])
    # sri_lanka = Album(service, "Sri Lanka")
    # print(sri_lanka)
    # media = Media(service,1)
    # print(media.get_media_map())
