# IMPORTS: #
import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


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
