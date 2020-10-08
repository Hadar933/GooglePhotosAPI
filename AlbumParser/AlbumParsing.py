"""
in this file we perform all the parsing that is relevant to an album. additing albums, iterating over albums, etc...
"""

# IMPOTRS: #
import os

from AlbumParser.Album import Album
from Initializer.InitializeData import create_service
import urllib.request

# CONSTANTS: #
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


def download_media_item(media_base_url, file_name):
    """
    downloads the content of media_url and names it file_name
    :param media_base_url: baseUrl field of some media item
    :param file_name: name to give the saved item
    """
    urllib.request.urlretrieve(media_base_url, file_name)


def download_album_content(album_name):
    """
    downloads the entire content of album_name and stores it in dir_name, which is a NEW directory
    """
    # TODO: theres a problem with the videos - they do not play
    album = instantiate_album(album_name)
    dir_name = album_name.replace(" ", "_") + "_content"
    os.mkdir(dir_name)
    media = album.get_media()
    downloaded = 0  # counter
    for item in media:
        base_url = item['baseUrl']
        name = item['filename']  # includes type
        path = dir_name + "/" + name
        download_media_item(base_url, path)
        downloaded += 1
        print("downloaded ", downloaded, "/", len(media), "(", name, ")")


def find_media_based_on_filter(filters, include_archive):
    """
    this function searches for media that corresponds to the given filter.
    note that this method is limited to the following filters:
    ANIMALS,FASHION,LANDMARKS,RECEIPTS,WEDDINGS,ARTS,FLOWERS,LANDSCAPES,SCREENSHOTS,WHITEBOARDS,BIRTHDAYS,FOOD,NIGHT
    SELFIES, CITYSCAPES,GARDENS,PEOPLE,SPORT, CRAFTS,HOLIDAYS,PERFORMANCES,TRAVEL,DOCUMENTS,HOUSES,PETS,UTILITY
    :param filters: a list of content categories (10 items max). using more than one filter is treated as
    searching filter1 AND filter2 AND ...
    :param include_archive: boolean indicating if the search should include the archive
    :return: lst of all relevant media
    """
    media_item_lst = []
    page_token = ""
    while True:
        body = {
            "pageToken": page_token if page_token != "" else "",
            "pageSize": 100,
            "filters": {
                "contentFilter": {
                    "includedContentCategories": filters
                },
                "includeArchivedMedia": include_archive
            }
        }
        curr = SERVICE.mediaItems().search(body=body).execute()
        media_items = curr.get(MEDIA_ITEM_ID, [])
        media_item_lst.extend(media_items)
        page_token = curr.get(NEXT_TOKEN_ID)
        if not page_token:
            break
    return media_item_lst


def scrape_name(person_name, media_url):
    """
    checks if some media item contains some person. for this to work, the data set should have a representation
    of photos and names given do it.
    :param person_name: a person we wish to loop for - must be the exact name as specified in the data set
    :param media_url: a url address of some media item
    :return: true: person in media. false otherwise
    """


def find_media_with_person(person_name,album):
    """
    we wrap the API media items search algorithm with a web scraper that searches the person_name in the data
    :param person_name: a string that represents the name of a person we wish to search for
    :param album: the album in which we wish to search (this is mainly provided because iterating over all media items
    is a long process, yet one can set album=None to iterate over all media items is he wishes)
    :return:
    """
