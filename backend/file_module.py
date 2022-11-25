"""Defines a file like module containing important information.

Classes: File
"""

import hashlib
import os


class File:
    """ File wrapper that contains important attributes of each file

        Methods:
            __init__(path)
            get_checksum(hash_factory=hashlib.md5, chunk_num_blocks=128)
            get_name()
            get_hash()

        Attributes:
            name -> Name of the file
            hash -> Hash generated from content of the file
            path -> Path to the file
    """
    name: str
    hash: bytes
    path: str

    def __init__(self, path):
        """Initializes the class using the given path

        Arguments:
            path -> Where to search for files

        """
        if os.path.exists(path):
            self.path = path
            self.get_checksum()
            self.get_name()
        else:
            print(path)
            raise Exception("File not created, path invalid")

    def get_checksum(self, hash_factory=hashlib.md5, chunk_num_blocks=128):
        """ Generates the MD5 hash of the file

        Arguments:
            hash_factory -> A MD5 library used to generate hashes
            chunk_num_blocks -> Defines the amount of Memory used

        """
        # Reference: https://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python
        hash_factory = hash_factory()
        with open(self.path, 'rb') as file_pointer:
            while chunk := file_pointer.read(chunk_num_blocks * hash_factory.block_size):
                hash_factory.update(chunk)
        self.hash = hash_factory.digest()

    def get_name(self):
        """ Returns the name of the file """
        self.name = os.path.basename(self.path)
        return str(self.name)

    def get_hash(self):
        """ Returns the hash of the file """
        return str(self.hash)
