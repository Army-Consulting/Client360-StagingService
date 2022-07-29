from APIUtil.APIDriver import APISetup
from dotenv import load_dotenv
import os

load_dotenv()

def main():

    MYAPISetUp = APISetup(os.environ["clientservicefilename"], os.environ["firebaseclientfilename"])
    MYAPISetUp.createSession()
    keys = MYAPISetUp.getSession()
    return 0

if __name__ == "__main__":
    main()