from dotenv import load_dotenv
from APISetupSheets.SheetCredentialsSetup import SheetsCredentialConnectorService
from google.oauth2.service_account import Credentials

from dotenv import load_dotenv
import os
load_dotenv()

def test_SheetCredentialSetup_void_file():
    # tests that a missing config file is considered an
    # IO error
    Sheetobject = SheetsCredentialConnectorService("test.jpg")
    assert Sheetobject.credentialSetUp() == "IO-ERROR"

def test_SheetCredential_incorrect_format():
    # tests that incorrectly formatted Google Sheets credentials are caught
    Sheetobject = SheetsCredentialConnectorService("../mocks/mock_sheets_credential.json")
    assert Sheetobject.credentialSetUp() == "Value Error"

def test_credentialSetUpRType():
    Sheetobject = SheetsCredentialConnectorService(os.environ["test_credentialSetUpRType"])
    assert type(Sheetobject.credentialSetUp()) is Credentials
