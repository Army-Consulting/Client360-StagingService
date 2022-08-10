from APIUtil.APIDriver import APISetup
from FBClient.StoreInterface import FirebaseRequest
from LinkUtil.GoogleSheetLink import SheetLinkFacade
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    t = date(2022, 4, 1)
    MYAPISetUp = APISetup(os.environ["clientservicefilename"], os.environ["firebaseclientfilename"])
    MYAPISetUp.createSession()
    keys = MYAPISetUp.getSession()
    FBR = FirebaseRequest(keys, SheetLinkFacade())
    FBR.PushUpdate("NS Training", t)
    return 0

if __name__ == "__main__":
    main()