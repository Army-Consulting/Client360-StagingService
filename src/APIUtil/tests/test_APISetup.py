from APIUtil.mocks.GoogleSheetObjs import (
    create_APISetup_incorect_fp, 
    create_API_Setup_incorrect_wrong_vals)

import pytest

# Tests that an APISetup object with an incorrect file path
# creates an IOError exception
def test_createSession_wrong_fp():
    with pytest.raises(IOError) as e_info:
        create_APISetup_incorect_fp().createSession()

# Tests that an APISetup object with an invalid json object
# creates an ValueError exception
def test_createSession_wrong_vals():
    with pytest.raises(ValueError) as e_info:
        create_API_Setup_incorrect_wrong_vals().createSession()
