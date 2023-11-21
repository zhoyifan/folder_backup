from sync_loop import SyncLoop
from folders.source_folder import SourceFolder
from folders.replica_folder import ReplicaFolder
from hashers.md5_hasher import MD5Hasher
import sys
def main():
    sourceFolder=SourceFolder('/media/z19941225110/HDD/workspace/python/test_task/sourceF')
    replicaFolder=ReplicaFolder('/media/z19941225110/HDD/workspace/python/test_task/replicaF')
    hasher=MD5Hasher()
    interval=5
    loop=SyncLoop(sourceFolder,replicaFolder,hasher,interval)
    loop.Loop()
    

if __name__ == "__main__":
    sys.path.append('./')
    main()
