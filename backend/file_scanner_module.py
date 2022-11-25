import os.path
from bisect import bisect_left
from Raspirus.backend.file_module import File


def bi_contains(lst, item):
    # Reference:
    # https://stackoverflow.com/questions/2701173/most-efficient-way-for-a-lookup-search-in-a-huge-list-python
    """ efficient `item in lst` for sorted lists """
    # if item is larger than the last its not in the list, but the bisect would
    # find `len(lst)` as the index to insert, so check that first. Else, if the
    # item is in the list then it has to be at index bisect_left(lst, item)
    return (item <= lst[-1]) and (lst[bisect_left(lst, item)] == item)


class FileScanner:
    # unscanned_list = List containing all files found in the specified path
    # clean_files = List of files whose hash is not listed
    # dirty_files = List of files whose hash is listed
    # hash_list = List of hashes
    unscanned_list = []
    clean_files = []
    dirty_files = []
    hash_list = []
    path = ""
    signature_db_path = ""

    def __init__(self, path, signature_path):
        # Checks if path is a directory and sets it to the class
        if os.path.isdir(path) and os.path.isfile(signature_path):
            self.path = path
            self.signature_db_path = signature_path
        else:
            print("Path: " + str(os.path.isdir(path)) + " & " + str(os.path.exists(path)))
            print("SignaturePath: " + str(os.path.isdir(signature_path)) +
                  " & " + str(os.path.exists(signature_path)))
            raise Exception("Invalid path or path not a directory")

    # Tries to open the file containing all hashes and read it line by line
    # Each line is then added to the hash_list
    def get_hash_list(self):
        try:
            with open(self.signature_db_path, encoding="utf8") as fp:
                for line in fp:
                    # Comments in the file need to be removed
                    if not line.startswith("#"):
                        self.hash_list.append(str(line))
        except FileNotFoundError as error:
            print("Error while reading the SignatureDB occured: " + str(error))

    # Finds all files in a specified path and adds them to the unscanned_list
    def get_file_list(self):
        for path, directories, file_names in os.walk(self.path):
            print("Directories found: " + str(directories))
            for file_name in file_names:
                file_path = path + "/" + file_name
                file = File(file_path)
                self.unscanned_list.append(file)

    # Compares each hash of a file with the hashes in the hash_list
    # If it finds something, the file is added to the dirty_files list
    def compare_lists(self):
        self.hash_list.sort()
        for file in self.unscanned_list:
            if bi_contains(self.hash_list, file.get_hash()):
                self.dirty_files.append(file)
            else:
                self.clean_files.append(file)

    ################################################################
    # These are the functions to start and initialize the scanner:
    ###############################################################

    # When initializing the scanner we fill the unscanned_list and hashes_list
    # After successfully doing so, we can start comparing the hashes
    def start_scanner(self):
        self.get_file_list()
        print("File list created! " + str(len(self.unscanned_list)) +
              " files found in " + self.path)
        self.get_hash_list()
        print("Hash list created! " + str(len(self.hash_list)) + " Hashes found")
        self.compare_lists()
        print("Scanner finished! \n"
              "Scanned files: " + str(len(self.unscanned_list)) + "\n"
              "Good files: " + str(len(self.clean_files)) + "\n"
              "Bad files: " + str(len(self.dirty_files)) + "\n"
              "Scanned path: " + self.path)
