"""
in this file we perform all the parsing that is relevant to an album. additing albums, iterating over albums, etc...
"""
from AlbumParser.Album import Album
from AlbumParser.DuplicateException import DuplicateException
from Initializer.InitializeData import create_service
from Main.InvalidInputException import InvalidInputException

ALBUMS_TO_SHOW = 50  # can only display 50 albums at once (maximum)

# MESSAGES: #
ALBUM_CREATION_SUCCESS_MSG = "AlbumParser {0} created successfully"
ALBUM_DUPLICATE_MSG = "AlbumParser {0} already exists. did not create album"
NO_ALBUM_MSG = "These isn't an album named: "

ALBUM_ID = "albums"  # identifier for the media item to be requested
NEXT_TOKEN_ID = "nextPageToken"  # identifier for the media item to be requested# DATASET: #

SERVICE = create_service()
ALL_ALBUMS = SERVICE.albums().list(pageSize=ALBUMS_TO_SHOW).execute()


def get_album_lst():
    """
    a helper method that returns a list of all albums, later to be converted to a dictionary
    """
    albums_lst = []
    page_token = ""
    token = page_token if page_token != "" else ""
    while True:
        curr = SERVICE.albums().list(pageSize=ALBUMS_TO_SHOW, pageToken=token).execute()
        albums = curr.get(ALBUM_ID, [])
        albums_lst.extend(albums)
        page_token = curr.get(NEXT_TOKEN_ID)
        if not page_token:
            break
    return albums_lst


def get_all_albums():
    """
    returns a dictionary of albums where the key is the album name and the value is an album object
    """
    album_dict = dict()
    album_lst = get_album_lst()
    for album in album_lst:
        media_id = album.get("id")
        title = album.get("title")
        product_url = album.get("productUrl")
        item_count = album.get("mediaItemsCount")
        cover_photo_url = album.get("coverPhotoBaseUrl")
        cover_photo_id = album.get("coverPhotoMediaItemId")
        album_dict[album.get("title")] = Album(media_id,title,product_url,item_count,cover_photo_url,cover_photo_id)
    return album_dict


def create_album(album_name):
    """
    creates an album with the given album name
    :param album_name: some string representing a wanted name
    :return: void
    """
    request_body = {"album": {"title": album_name}}
    SERVICE.albums().create(body=request_body).execute()
    print(ALBUM_CREATION_SUCCESS_MSG.format(album_name))



