from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from google.oauth2.service_account import Credentials
from google.auth.exceptions import MutualTLSChannelError

import json

class SheetsCredentialConnectorService:

    def __init__(self, configFile):
        self.configfile = configFile

    def credentialSetUp(self):
        try:
            billing_project_credential_json = open(self.configfile)
        except IOError:
            return IOError
        billing_project_account = json.load(billing_project_credential_json)
        try:
            credentials = service_account.Credentials.from_service_account_info(billing_project_account)
        except ValueError:
            return ValueError
        scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/spreadsheets'])
        return scoped_credentials

class SheetsCredentialConnectorConsumer:

    def __init__(self, CredentialConnector: Credentials):
        self.credentialconnector = CredentialConnector

    def activate(self):
        credentials = self.credentialconnector.credentialSetUp()
        if(credentials == IOError):
            raise IOError
        elif(credentials == ValueError):
            raise ValueError
        else:
            try:
                service = build('sheets', 'v4', credentials=credentials)
                return service
            except MutualTLSChannelError:
                return MutualTLSChannelError