from sync_loop import SyncLoop
from folders.source_folder import SourceFolder
from folders.replica_folder import ReplicaFolder
from hashers.md5_hasher import MD5Hasher
import sys
import logging
import argparse
import os
def PreprocessDirectory(directory):
    if not os.path.isabs(directory):
        return os.path.abspath(os.path.join(os.getcwd(),directory))
    return directory
def ParseArgs():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Synchronize files from the source folder to the replica folder.')
    parser.add_argument('-s','--source', type=str,
                    help='Assign source folder directory, to be syncronized to the replica folder.',
                    default='./sourceF')
    parser.add_argument('-r','--replica', type=str,
                    help='Assign replica folder directory, syncronize files from the source folder.',
                    default='./replicaF')
    parser.add_argument('-i','--interval',type=int,
                    help='How many seconds to wait between two sycronizations.',
                    default=5)
    parser.add_argument('-l','--log',type=str,
                    help='Assign log file path, to record the program behaviour.',
                    default='./sync.log')
    args = parser.parse_args()
    args.source=PreprocessDirectory(args.source)
    args.replica=PreprocessDirectory(args.replica)
    args.log=PreprocessDirectory(args.log)
    return args
def main():

    
    args=ParseArgs()
    sourceFolder=SourceFolder(args.source)
    replicaFolder=ReplicaFolder(args.replica)
    hasher=MD5Hasher()
    interval=args.interval
    


    # logging.info("ssdlsls")
    
    logger=logging.getLogger()
    logger.setLevel(logging.INFO)
    fileHandler=logging.FileHandler(args.log)
    streamHandler=logging.StreamHandler()
    
    def AddHandler(logger,handler):
        logFormat=logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
        handler.setFormatter(logFormat)
        logger.addHandler(handler)
    AddHandler(logger,fileHandler)
    AddHandler(logger,streamHandler)
    loop=SyncLoop(sourceFolder,replicaFolder,hasher,interval)
    loop.Loop()
    

if __name__ == "__main__":
    sys.path.append('./')
    main()
