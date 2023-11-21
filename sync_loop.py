import time
from folders.source_folder import SourceFolder
from folders.replica_folder import ReplicaFolder
from hashers.hasher import Hasher
class SyncLoop:
    def __init__(self,sourceFolder:SourceFolder,replicaFolder:ReplicaFolder,hasher:Hasher,interval:int):
        self.sourceFolder=sourceFolder
        self.replicaFolder=replicaFolder
        self.hasher=hasher
        self.interval=interval
    def Loop(self):
        while(True):
            time.sleep(self.interval)
            self.sourceFolder.CalculateHashes(self.hasher)
            self.replicaFolder.DeleteFiles(self.sourceFolder)
            self.replicaFolder.AddOrUpdateFiles(self.sourceFolder)
            self.replicaFolder.DeleteSubFolders(self.sourceFolder)
            self.replicaFolder.AddSubFolders(self.sourceFolder)
            
    
