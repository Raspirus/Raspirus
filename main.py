from backend.FileScanner import FileScanner
from backend.HashAPI import HashAPI

# This function isn't finished yet and used for testing purposes, will then be implemented later
def main():
    print("#########################################################################")
    print("# Insert a directory to scan and the scanner will start automatically!  #")
    print("# Path syntax: 'C:/Users/someone/Documents/ToScan'                      #")
    print("# REMEMBER! No '/' at the end and no '                                  #")
    print("#########################################################################")
    # Example: C:/Users/benbe/Documents/Coding/WebProjects
    path_to_check = str(input("Enter path: "))
    print("")
    path_to_signatures = "C:/Users/benbe/Documents/School/MaturaProject/Github/backend/BigHash.db"
    fs = FileScanner(path_to_check, path_to_signatures)
    fs.start_scanner()

def updater():
    # Path to directory with md5 files/file extension, path to the bighash file
    hapi = HashAPI("backend/SignatureLists/*md5", "backend/BigHash.db")
    h_list = hapi.get_hash()
    print("Length: " + str(len(h_list)))


updater()
