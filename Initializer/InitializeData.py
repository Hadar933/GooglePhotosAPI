import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

API_NAME = 'photoslibrary'
API_VERSION = 'v1'
CLIENT_SECRET_FILE = '../client_Secret.json'
READ_WRITE_SCOPE = ['https://www.googleapis.com/auth/photoslibrary']
SHARE_SCOPE = ['https://www.googleapis.com/auth/photoslibrary.sharing']
SCOPES = [READ_WRITE_SCOPE, SHARE_SCOPE]


def create_service():
    """
    a function that generates a service to work on from given data
    mostly provided by Jie Jenn (youtube)
    :return: the service, or null
    """

    client_secret_file = '../client_Secret.json'
    api_name = 'photoslibrary'
    api_version = 'v1'
    read_write_scope = ['https://www.googleapis.com/auth/photoslibrary']
    share_scope = ['https://www.googleapis.com/auth/photoslibrary.sharing']
    all_scopes = [read_write_scope, share_scope]

    all_scopes = [scope for scope in all_scopes[0]]
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
                client_secret_file, all_scopes)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    service = build(api_name, api_version, credentials=cred)
    print(api_name, 'service created successfully')
    return service
