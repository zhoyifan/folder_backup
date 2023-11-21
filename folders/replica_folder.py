from folders.folder import Folder
from folders.source_folder import SourceFolder
from pathlib import Path
import shutil
import os
import logging

class ReplicaFolder(Folder):
    def __init__(self, directory):
        super().__init__(directory)
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.mkdir(directory)
        
    def DeleteFiles(self,sourceFolder:SourceFolder):
        sourceHashes=sourceFolder.GetHashes()
        toDelete=[]
        for filePath,hash in self.hashes.items():
            if filePath not in sourceHashes:
                Path.unlink(Path(os.path.join(self.directory,filePath)))
                toDelete.append(filePath)
        for i in toDelete:
            self.hashes.pop(i,None)
            logging.info(f"File {i} deleted.")

    def AddOrUpdateFiles(self,sourceFolder:SourceFolder):
        sourceHashes=sourceFolder.GetHashes()
        for filePath,hash in sourceHashes.items():
            if filePath not in self.hashes or hash!=self.hashes[filePath]:
                sourceFilePath=os.path.join(sourceFolder.directory,filePath)
                replicaFilePath=os.path.join(self.directory,filePath)
                replicaFilePath=os.path.join(replicaFilePath,os.pardir)
                replicaFilePath=os.path.abspath(replicaFilePath)
                # replicaFilePath=os.path.join(replicaFilePath,'/')
                if not os.path.exists(replicaFilePath):
                    os.mkdir(replicaFilePath)
                    logging.info(f'Folder {replicaFilePath} created.')
                shutil.copy(sourceFilePath, replicaFilePath)
                logging.info(f'File copied from {sourceFilePath} to {replicaFilePath}')
                self.hashes[filePath]=hash
    
    def DeleteSubFolders(self,sourceFolder:SourceFolder):
        sourceSubfolders=sourceFolder.GetSubfolders()
        toRemove=[]
        for subfolder in self.subfolders:
            if subfolder not in sourceSubfolders:
                shutil.rmtree(os.path.join(self.directory,subfolder))
                toRemove.append(subfolder)
        for i in toRemove:
            self.subfolders.remove(i)
            logging.info(f'File {i} deleted.') 
    def AddSubFolders(self,sourceFolder:SourceFolder):
        sourceSubfolders=sourceFolder.GetSubfolders()
        for subfolder in sourceSubfolders:
            if subfolder not in self.subfolders:
                os.makedirs(os.path.join(self.directory,subfolder),exist_ok=True)
                self.subfolders.add(subfolder)
                logging.info(f'Folder {os.path.join(self.directory,subfolder)} created.')

        
