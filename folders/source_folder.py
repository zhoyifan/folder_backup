from folders.folder import Folder
from hashers.hasher import Hasher
# from ..hashers.md5_hasher import MD5Hasher
import os
class SourceFolder(Folder):
    def __init__(self, directory):
        super().__init__(directory)
    def CalculateHashes(self,hasher:Hasher):
        self.hashes=dict()
        filePaths=self.FetchAllFilePathsAndSubfolders()
        for filePath in filePaths:
            self.hashes[filePath]=hasher.Hashing(os.path.join(self.directory,filePath))
            

        