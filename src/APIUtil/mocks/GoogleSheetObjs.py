from APIUtil.APIDriver import APISetup

from dotenv import load_dotenv
import os
load_dotenv()

# APISetup object that has incorrect filepath for google sheet
def create_APISetup_incorect_fp():
    return APISetup("test.json", "test.json")
    
# APISetup object that has incorrect json values/properties
# Assume FBS credential path is correct:
def create_API_Setup_incorrect_wrong_vals():
    return APISetup("../mocks/mock_sheets_credential.json", os.environ["test_FBScredentialSetUpRType"])