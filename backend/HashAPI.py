import os.path
import shutil
import glob


# This class will do the following tasks using the Virusshare API
# - Periodically check if new hash signatures are available
# - Remove Hashes that are found twice in files
# - If needed, find more specific data on a Hash
# - Update the Hash signatures

class HashAPI:
    api_key = ""
    bighash_path = ""
    signature_list_path = ""
    hash_list = list()
    file_list = list()

    def __init__(self, signature_path, bighash_path):
        self.signature_list_path = signature_path
        self.bighash_path = bighash_path
        self.file_list = glob.glob(self.signature_list_path)
        self.update_bighash()

    def get_hash(self):
        return self.hash_list

    # A function to merge all hash lists into one
    def merge_files(self):
        with open(self.bighash_path, 'wb') as wfd:
            # 38797309 Hash
            for f in self.file_list:
                with open(f, 'rb') as fd:
                    shutil.copyfileobj(fd, wfd)

    def refactor_bighash(self):
        # Extract all hashes from file and put them into an array
        # then overwrite the file with this array and put a message at the end of the file
        # The message will then specify the last merged file
        # This is useful to later detect which file still needs to be added

        # Read all hashes from file
        with open(self.bighash_path) as fp:
            for line in fp:
                # Comments in the file need to be removed
                if not line.startswith("#"):
                    self.hash_list.append(str(line))

        # Write all hashes to file
        with open(self.bighash_path, 'w') as fp:
            for hashes in self.hash_list:
                fp.writelines(hashes + "\n")
            # Write last line to identify which Hash we included for last
            fp.writelines("# Last added: " + self.file_list[len(self.file_list) - 1])

    def bighash_is_updated(self):
        # If the name of the file mentioned in the last line of bighash is the same as the last item in file_list
        # we consider the file as updated
        if os.path.exists(self.bighash_path):
            with open(self.bighash_path, 'rb') as f:
                try:  # catch OSError in case of a one line file
                    f.seek(-2, os.SEEK_END)
                    while f.read(1) != b'\n':
                        f.seek(-2, os.SEEK_CUR)
                except OSError:
                    f.seek(0)
                last_line = f.readline().decode()
                print(last_line)
                print(last_line.split("added:", 1)[1])
                print(self.file_list[len(self.file_list) - 1])
                if last_line.split("added:", 1)[1] == self.file_list[len(self.file_list) - 1]:
                    return True
                else:
                    return False
        else:
            return False

    def update_bighash(self):
        # First check if the file exists, then if the latest hash list has been added
        if self.bighash_is_updated():
            pass
        else:
            self.file_list = glob.glob(self.signature_list_path)
            self.merge_files()
            self.refactor_bighash()
        pass

    def download_hash(self):
        # Downloads new hashes from Virusshare if available
        pass

    def get_hash_info(self, vhash):
        # Retrieves more detailed information about a specific hash by using the Virusshare API
        pass
