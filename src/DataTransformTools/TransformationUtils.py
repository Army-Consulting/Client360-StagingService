from .MonthDataModel import MonthDataDictionary

# Capture document reference
def pushupdate(TS, Company, employeeTimeSheetList, serviceproviders):
    # Establish the companies collection that holds the 'company' documents
    Year2022_ref_COL = serviceproviders['FBStore'].collection("Y" + TS['year']).document("M-"+TS['month']+TS['year']).collection(TS['month']+TS['year'] + "-Companies")
    UpdateObject = CreateUpdateObject(employeeTimeSheetList, TS['month'], Company, serviceproviders)
    Year2022_ref_COL.document(Company).set(UpdateObject)

def CreateUpdateObject(employeeTimeSheetList, month, companyName, serviceproviders):
    # Create master DayObj
    MasterObj = MonthDataDictionary()
    # Records from each employee timesheet appended to the master
    for API_LINK in employeeTimeSheetList.getSheetLinks():
        PopulateMasterObject(API_LINK, month, companyName, MasterObj, serviceproviders)
    return {x:list(y) for x,y in MasterObj.GetMonthDataDict().items()}

def PopulateMasterObject(timeSheetID, month, company, masterobj, serviceproviders):
    Payload = CaptureEmployeeTimeSheetData(timeSheetID, month, serviceproviders)
    for i in range(0, len(Payload)):
        FillRecords(Payload[i], i, company, masterobj)
        
def CaptureEmployeeTimeSheetData(timeSheetID, month, serviceproviders):
    TimeKeepingPayload = serviceproviders['GoogleSheets'].spreadsheets().values().get(spreadsheetId=timeSheetID, range=f"{month}!A6:CS29").execute()
    return TimeKeepingPayload.get('values')

## Fill dictionary
def FillRecords(HourRow, HourNumber, CompName, DayObj):
    if(CompName in HourRow):
        currentDay, CompNamePtr, DescPtr = 1, 4, 5
        for day in range(currentDay, 32):
            if(HourRow[CompNamePtr] == CompName and len(HourRow[DescPtr])):
                #DayObj[str(day)].append({"Note": HourRow[DescPtr], "Config":{}})
                DayObj.AddData(str(day), {"Note": HourRow[DescPtr], "Config":{}})
            CompNamePtr += 3
            DescPtr += 3