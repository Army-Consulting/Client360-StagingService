from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin.exceptions import FirebaseError
import firebase_admin

class FirebaseCredentialConnectorService:
    def __init__(self, configFile):
        self.configfile = configFile
    def credentialSetUp(self):
        try:
            fbcred = credentials.Certificate(self.configfile)
        except IOError:
            return IOError
        except ValueError:
            return ValueError
        return fbcred

class FirebaseCredentialConnectorConsumer:
    def __init__(self, CredentialConnector):
        self.credentialconnector = CredentialConnector
    def activate(self):
        credentials = self.credentialconnector.credentialSetUp()
        if(credentials == IOError):
            raise IOError
        elif(credentials == ValueError):
            raise ValueError
        else:
            try:
                firebase_admin.initialize_app(credentials)
                store = firestore.client()
                return store
            except FirebaseError as error:
                return None

