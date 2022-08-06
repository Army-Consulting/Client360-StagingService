from ast import Assert
import pytest
from APISetupSheets.SheetCredentialsSetup import SheetsCredentialConnectorService

def test_SheetCredentialSetup_void_file():
    # tests that a missing config file is considered an
    # IO error
    Sheetobject = SheetsCredentialConnectorService("test.jpg")
    assert Sheetobject.credentialSetUp() == "IO-ERROR"

def test_SheetCredential_incorrect_format():
    # tests that incorrectly formatted Google Sheets credentials are caught
    Sheetobject = SheetsCredentialConnectorService("/Users/briandavid/Projects/Client360/src/APISetupSheets/mocks/mock_sheets_credential.json")
    assert Sheetobject.credentialSetUp() == "Value Error"