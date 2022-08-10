from APISetupFBS.FirebaseStoreSetUp import FirebaseCredentialConnectorService
from APISetupFBS.FirebaseStoreSetUp import FirebaseCredentialConnectorConsumer
from google.cloud.firestore_v1.client import Client
from dotenv import load_dotenv
import os
import pytest

load_dotenv()

def test_FirebaseCredentialConsumer_IncorrectRoot():
    FCCS = FirebaseCredentialConnectorService("test.json")
    FCCC = FirebaseCredentialConnectorConsumer(FCCS)
    with pytest.raises(IOError) as e_info:
        FCCC.activate()

def test_FirebaseCredentialConsumer_IncorrectFrmt():
    FCCS = FirebaseCredentialConnectorService("../mocks/mock_fbs_credential.json")
    FCCC = FirebaseCredentialConnectorConsumer(FCCS)
    with pytest.raises(ValueError) as e_info:
        FCCC.activate()

def test_FirebaseCredentialConsumer_IncorrectCredentials():
    FCCS = FirebaseCredentialConnectorService("../mocks/mock_fbs_credential_wrong_val.json")
    FCCC = FirebaseCredentialConnectorConsumer(FCCS)
    with pytest.raises(ValueError) as e_info:
        FCCC.activate()

def test_credentialSetUpRType():
    FCCS = FirebaseCredentialConnectorService(os.environ["test_credentialSetUpRType"])
    FCCC = FirebaseCredentialConnectorConsumer(FCCS)
    assert type(FCCC.activate()) is Client
