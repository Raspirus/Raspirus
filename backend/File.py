import hashlib
import os


class File:
    name = ""
    hash = ""
    path = ""

    def __init__(self, path):
        if os.path.exists(path):
            self.path = path
            self.get_checksum()
            self.get_name()
        else:
            print(path)
            raise Exception("File not created, path invalid")

    def get_checksum(self, hash_factory=hashlib.md5, chunk_num_blocks=128):
        # Reference: https://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python
        h = hash_factory()
        with open(self.path, 'rb') as f:
            while chunk := f.read(chunk_num_blocks * h.block_size):
                h.update(chunk)
        self.hash = h.digest()

    def get_name(self):
        self.name = os.path.basename(self.path)
        return str(self.name)

    def get_hash(self):
        return str(self.hash)
