from pytest_mock import mocker
from DataTransformTools.mocks import Constants
from DataTransformTools.TransformationUtils import (PopulateMasterObject,
    CaptureEmployeeTimeSheetData, pushupdate)
from APIUtil.APIDriver import APIConfig
from DataTransformTools.MonthDataModel import MonthDataDictionary
from dotenv import load_dotenv
from googleapiclient.errors import HttpError
from datetime import date
from DataTransformTools.TimestampTool import Timestamp
from google.api_core.exceptions import RetryError
import pytest
import os

load_dotenv()

# Global testing_config
test_config = APIConfig()
test_config.activateSheets(os.environ["test_TransformationUtils_clientsheets"])
test_config.activateFirebase(os.environ["test_TransformationUtils_FBS"])

# testing PopulateMasterObject functionality - complete 31 days
def test_PopulateMasterObject(mocker):
    # Mock the CaptureEmployeeTimeSheetData API Call function
    mocker.patch(
        'DataTransformTools.TransformationUtils.CaptureEmployeeTimeSheetData', 
        return_value=Constants.TIMEKEEPINGPAYLOAD31)
    myMonth = MonthDataDictionary()
    PopulateMasterObject("specialID", "April", "NS Training", myMonth, {"A":1, "B":2})
    assert {x:list(y) for x,y in myMonth.GetMonthDataDict().items()} == Constants.FILLEDMONTHDICT31

# testing CaptureEmployeeTimeSheetData with an incorrect spreadsheet link
def test_CaptureEmployeeTimeSheetDataNoConnection():
    # create GoogleSheet credentials
    with pytest.raises(HttpError) as e_info:
        CaptureEmployeeTimeSheetData("xbdfgbkrhgdg", 
        "may", 
        {'GoogleSheets': test_config.getSheetService()})

# testing CaptureEmployeeTimeSheetData with an incorrect month that does not yet exist
def test_CaptureEmployeeTimeSheetDataNonexistingMonth():
    # create GoogleSheet credentials
    with pytest.raises(HttpError) as e_info:
        CaptureEmployeeTimeSheetData(os.environ["test_TransformationUtils_clientsheets_link"], 
        "NoMonth", 
        {'GoogleSheets': test_config.getSheetService()})

# test push update setting a document with no connection 
def test_PushUpdateSetNoConnection(mocker):
    # Mock the CreateUpdateObject API Call function
    ts = date(2022, 4, 1)
    mocker.patch(
        'DataTransformTools.TransformationUtils.CreateUpdateObject', 
        return_value=Constants.FILLEDMONTHDICT31)
    with pytest.raises(RetryError) as e_info:
        pushupdate(Timestamp(ts).TimestampToFirebaseString(), 
        'NS Training', 
        ["SheetID1", "SheetID2"],
        {'FBStore': test_config.getFirebaseStore()})
    