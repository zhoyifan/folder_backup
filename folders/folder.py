import os,sys

class Folder:
    def __init__(self,directory):
        self.directory=directory
        self.hashes=dict()
        self.subfolders=set()
    def GetHashes(self):
        return self.hashes
    def GetSubfolders(self):
        return self.subfolders
    def FetchAllFilePathsAndSubfolders(self):
        resPaths=[]
        self.subfolders=set()
        def lsdir(directory:str):
            contents = os.listdir(os.path.join(self.directory,directory))
            # print "%s\n%s\n" % (directory, contents)
            for path in contents:
                full_path = os.path.join(self.directory,directory,path)
                if os.path.isdir(full_path):
                    self.subfolders.add(os.path.join(directory,path))
                    lsdir(os.path.join(directory,path))
                else:
                    resPaths.append(os.path.join(directory,path))
        lsdir('')
        return resPaths


