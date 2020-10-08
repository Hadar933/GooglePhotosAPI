GooglePhotosAPI wrapper (Python) - performs various operations on your google photos media
-------------------------------------------------------------------------------

### created by:

Hadar Sharvit

-------------------------------------------------------------------------------
### Latest Feature:

download the content of some album to your pc - use AlbumParsing.download_album_content(album_name)

-------------------------------------------------------------------------------

### Description:

this is a basic project that enhances the performance of the google photos API.
it enables some more specific operations and content manipulation to your media

-------------------------------------------------------------------------------

### Try it yourself:

#### create a google cloud platform
 
  google demands -  in order to use their API, one must open an account here:  `https://console.cloud.google.com/` (denoted `LINK`)
  
  the full google photos API can be found here:  `https://developers.google.com/photos/library/guides/overview` 
  
  the links also contain some guidance, but here is a quick summary of what you need to do:
   * in `LINK`, create a new project in google cloud platforms
   * in `LINK`, under API's & Services > Library, search for Google Photos API and click ENABLE
   * in `LINK`, under API's & Services > credentials, create an OAuth ID. this will create your client secret file, DOWNLOAD it and save it in the project repository.
     (more on that later)
   * install some google packages, (use: `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`)
   * install pandas package (use: `pip install pandas`)
   
#### running the program:

  once you've followed the rules of the previous segment, you should have a folder called something like client_secret.
  make sure to keep the content secret (obviously), for it contains some private data regarding your google account.
  add the path of the file under 
  `CLIENT_SECRET_FILE`
  and use the program as you'd like. 
  
-------------------------------------------------------------------------------
  
#### Remarks
  1. some methods may delete your media, so make sure you read the documentation!!
  
  2. currently a work in progress. More elaborate documentation will be added in the future
  
