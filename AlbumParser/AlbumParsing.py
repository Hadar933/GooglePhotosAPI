"""
in this file we perform all the parsing that is relevant to an album. additing albums, iterating over albums, etc...
"""

# CONSTANTS: #
from AlbumParser.Album import Album
from Initializer.InitializeData import create_service

MEDIA_TO_SHOW = 100  # can only display 100 media items at once
ALBUMS_TO_SHOW = 50  # can only display 50 albums at once

# MESSAGES: #
ALBUM_CREATION_SUCCESS_MSG = "AlbumParser {0} created successfully"
ALBUM_DUPLICATE_MSG = "AlbumParser {0} already exists. did not create album"
NO_ALBUM_MSG = "These isn't an album named: "

ALBUM_ID = "albums"  # identifier for the media item to be requested
NEXT_TOKEN_ID = "nextPageToken"  # identifier for the media item to be requested# DATASET: #
MEDIA_ITEM_ID = "mediaItems"  # identifier for the media item to be requested

SERVICE = create_service()


def get_albums_dict():
    """
    a method that returns a dict of all albums.
    Note: I chose to not initialize the data set where each element is an Album object, because
    fetching the media for each album is a long process. this will happen only when instantiating
    """
    albums_lst = []
    album_dict = dict()
    page_token = ""
    token = page_token if page_token != "" else ""
    while True:
        curr = SERVICE.albums().list(pageSize=ALBUMS_TO_SHOW, pageToken=token).execute()
        albums = curr.get(ALBUM_ID, [])
        albums_lst.extend(albums)
        page_token = curr.get(NEXT_TOKEN_ID)
        if not page_token:
            break
    for album in albums_lst:
        album_dict[album.get("title")] = album
    return album_dict


def instantiate_album(title):
    """
    returns an album object from the given title
    """
    album_dict = get_albums_dict()
    album = album_dict[title]
    media_id = album.get("id")
    product_url = album.get("productUrl")
    item_count = album.get("mediaItemsCount")
    cover_photo_url = album.get("coverPhotoBaseUrl")
    cover_photo_id = album.get("coverPhotoMediaItemId")
    return Album(media_id, title, product_url, item_count, cover_photo_url, cover_photo_id)


def create_album(album_name):
    """
    creates an album with the given album name
    :param album_name: some string representing a wanted name
    :return: void
    """
    request_body = {"album": {"title": album_name}}
    SERVICE.albums().create(body=request_body).execute()
    print(ALBUM_CREATION_SUCCESS_MSG.format(album_name))


def get_media_in_album(id):
    """
    this method returns a dictionary that contains all the media that is relevant to this album (key = media id)
    """
    media_item_lst = []
    page_token = ""
    while True:
        body = {
            "albumId": id,
            "pageToken": page_token if page_token != "" else "",
            "pageSize": MEDIA_TO_SHOW
        }
        curr = SERVICE.mediaItems().search(body=body).execute()
        media_items = curr.get(MEDIA_ITEM_ID, [])
        media_item_lst.extend(media_items)
        page_token = curr.get(NEXT_TOKEN_ID)
        if not page_token:
            break
    return media_item_lst


def find_album_by_name(name, all_albums):
    """
    finds the album with the given name in the dataset
    :param name: some name of an album
    :param all_albums: the data set of all the albums (dictionary)
    :return:
    """
    for album in all_albums:
        if album == name:
            return all_albums[album]
    return None
