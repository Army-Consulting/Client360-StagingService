from APISetupFBS.FirebaseStoreSetUp import FirebaseCredentialConnectorService
from APISetupFBS.FirebaseStoreSetUp import FirebaseCredentialConnectorConsumer
import pytest

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