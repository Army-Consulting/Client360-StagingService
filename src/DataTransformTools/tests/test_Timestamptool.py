from DataTransformTools.TimestampTool import Timestamp
from datetime import date


mock_date = date(2022, 8, 1)
mock_TSClass = Timestamp(mock_date)

mock_futureDate = date(2023, 8, 1)
mock_futureTSClass = Timestamp(mock_futureDate)

def test_correctFirebaseString():
    # initialize date object
    assert mock_TSClass.TimestampToFirebaseString() == {"month": "August", "year": "2022"}

def test_inputIsAtOrBeforePresentDate():
    assert mock_TSClass.IsTimestampBefore() is True

def test_inputDoesNotExceedPresentDate():
    assert mock_futureTSClass.IsTimestampBefore() is False
