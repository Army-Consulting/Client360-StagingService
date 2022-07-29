from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin.exceptions import FirebaseError
import firebase_admin
import json

class FirebaseCredentialConnectorService:
    def __init__(self, configFile):
        self.configfile = configFile
    def credentialSetUp(self):
        firebase_acct_info_file = open(self.configfile)
        firebase_acct_info = json.load(firebase_acct_info_file)
        fbcred = credentials.Certificate(self.configfile)
        return fbcred

class FirebaseCredentialConnectorConsumer:
    def __init__(self, CredentialConnector):
        self.credentialconnector = CredentialConnector
    def activate(self):
        credentials = self.credentialconnector.credentialSetUp()
        try:
            firebase_admin.initialize_app(credentials)
            store = firestore.client()
            return store
        except FirebaseError as error:
            return None

