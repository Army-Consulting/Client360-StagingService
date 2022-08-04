from DataTransformTools.TransformationUtils import pushupdate
from DataTransformTools.TimestampTool import Timestamp

class FirebaseRequest:
    def __init__(self, serviceProviders, UserLinks):
        self.CompanyLists = ["NS Training", "WSI"]
        UserLinks.capture()
        self.EmployeeSheetLinks = UserLinks
        self.serviceproviders = serviceProviders
        
    def PushUpdate(self, Company, TS):
        # Establish the companies collection that holds the 'company' documents
        if(Company not in self.CompanyLists):
            raise Exception(f"{Company} does not exist in the staging database")
        if(not Timestamp(TS).IsTimestampBefore()):
            raise Exception(f"Timestamp exceeds present date")
            
        pushupdate(Timestamp(TS).TimestampToFirebaseString(), Company, self.EmployeeSheetLinks, self.serviceproviders)