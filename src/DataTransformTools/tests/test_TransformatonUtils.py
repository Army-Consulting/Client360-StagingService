from pytest_mock import mocker
from DataTransformTools.mocks import Constants
from DataTransformTools.TransformationUtils import PopulateMasterObject
from DataTransformTools.MonthDataModel import MonthDataDictionary

# testing PopulateMasterObject - complete 31 days
def test_PopulateMasterObject(mocker):
    # Mock the CaptureEmployeeTimeSheetData API Call function
    mocker.patch(
        'DataTransformTools.TransformationUtils.CaptureEmployeeTimeSheetData', 
        return_value=Constants.TIMEKEEPINGPAYLOAD31)
    myMonth = MonthDataDictionary()
    PopulateMasterObject("specialID", "April", "NS Training", myMonth, {"A":1, "B":2})
    assert {x:list(y) for x,y in myMonth.GetMonthDataDict().items()} == Constants.FILLEDMONTHDICT31

