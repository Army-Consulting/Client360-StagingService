from dotenv import load_dotenv
import pytest
from APISetupSheets.SheetCredentialsSetup import SheetsCredentialConnectorConsumer, SheetsCredentialConnectorService
from APISetupSheets.SheetCredentialsSetup import SheetsCredentialConnectorService
from google.oauth2.service_account import Credentials

from dotenv import load_dotenv
import os
load_dotenv()

def test_credentialSetUpRType():
    Sheetobject = SheetsCredentialConnectorService(os.environ["test_credentialSetUpRType"])
    assert type(Sheetobject.credentialSetUp()) is Credentials

def test_SheetCredentialCCActivate_IncorrectRoot():
    Sheetobject = SheetsCredentialConnectorService("test.jpg")
    SCCS = SheetsCredentialConnectorConsumer(Sheetobject)
    with pytest.raises(IOError) as e_info:
        SCCS.activate()

def test_SheetCredentialCCActivate_IncorrectFrmt():
    Sheetobject = SheetsCredentialConnectorService("../mocks/mock_sheets_credential.json")
    SCCS = SheetsCredentialConnectorConsumer(Sheetobject)
    with pytest.raises(ValueError) as e_info:
        SCCS.activate()