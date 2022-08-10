from APISetupSheets.SheetCredentialsSetup import SheetsCredentialConnectorService
from APISetupSheets.SheetCredentialsSetup import SheetsCredentialConnectorConsumer
from APISetupFBS.FirebaseStoreSetUp import FirebaseCredentialConnectorService
from APISetupFBS.FirebaseStoreSetUp import FirebaseCredentialConnectorConsumer

class APIConfig:
    def __init__(self):
        self.SheetService = None
        self.FirebaseStore = None

    def activateSheets(self, sheetConfig):
        SCCS = SheetsCredentialConnectorService(sheetConfig)
        SCCC = SheetsCredentialConnectorConsumer(SCCS)
        try:
            self.SheetService = SCCC.activate()
        except IOError:
            raise IOError
        except ValueError:
            raise ValueError
    
    def activateFirebase(self, firebaseConfig):
        FCCS = FirebaseCredentialConnectorService(firebaseConfig)
        FCCC = FirebaseCredentialConnectorConsumer(FCCS)
        try:
            self.FirebaseStore = FCCC.activate()
        except IOError:
            raise IOError
        except ValueError:
            raise ValueError
    
    def getSheetService(self):
        return self.SheetService
    
    def getFirebaseStore(self):
        return self.FirebaseStore

class APISetup:
    def __init__(self, SheetsJSONFile, FirebaseJSONFile):
        self.sheetsjsonfile = SheetsJSONFile
        self.firebasejsonfile = FirebaseJSONFile
        self.apiconfig = APIConfig()
    
    def createSession(self):
        self.apiconfig.activateSheets(self.sheetsjsonfile)
        self.apiconfig.activateFirebase(self.firebasejsonfile)
    
    def getSession(self):
        GS = self.apiconfig.getSheetService()
        FBS = self.apiconfig.getFirebaseStore()
        if(not GS and not FBS):
            raise ConfigError
        else:
            return {'GoogleSheets': GS,'FBStore': FBS}

class ConfigError(Exception):
    """Exception when either Sheets or FBS connection is mishandled"""
    
    def __init__(self, message = "Interruption occurred when configuring Sheets & FBS API"):
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return self.message