from DataTransformTools.MonthDataModel import MonthDataDictionary
from DataTransformTools.mocks import Constants
test_MDD = MonthDataDictionary()

def test_CompletedDataAddition():
    test_MDD.AddData("1", 
    {"Note":"testNote", "Config": {}
    })
    assert test_MDD.GetMonthDataDict() == Constants.ONEENTRY
