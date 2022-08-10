from APISetupFBS.FirebaseStoreSetUp import FirebaseCredentialConnectorService
from APISetupFBS.FirebaseStoreSetUp import FirebaseCredentialConnectorConsumer
import pytest

def test_FirebaseCredentialConsumer_IncorrectRoot():
    FCCS = FirebaseCredentialConnectorService("test.json")
    FCCC = FirebaseCredentialConnectorConsumer(FCCS)
    with pytest.raises(IOError) as e_info:
        FCCC.activate()