from APIUtil.APIDriver import APIConfig
import pytest

def test_activateSheets_incorrect_fp():
    with pytest.raises(IOError) as e_info:
        APIConfig().activateSheets("test.json")

def test_activateSheets_incorrect_frmt():
    with pytest.raises(ValueError) as e_info:
        APIConfig().activateSheets("../mocks/mock_sheets_credential.json")

def test_activateSheets_incorrect_vals():
    with pytest.raises(Exception) as e_info:
        APIConfig().activateSheets("../mocks/mock_sheets_credential_wrong_val.json")

