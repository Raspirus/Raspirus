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
    # 38797306 Hashes
    hapi = HashAPI("backend/SignatureLists/*md5", "backend/BigHash.db")
    hapi.update_bighash()
    h_list = hapi.get_hash()
    print("Length: " + str(len(h_list)))

def downloader():
    hapi = HashAPI("backend/SignatureLists/*md5", "backend/BigHash.db")
    hapi.download_new_signatures("backend/SignatureLists")

def more_info():
    hapi = HashAPI("backend/SignatureLists/*md5", "backend/BigHash.db")
    hapi.get_hash_info("backend/temp/test.json", "ecb9cf121345c404495d99c737c7d3bf")

updater()
