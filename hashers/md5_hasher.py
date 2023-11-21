import hashlib
from .hasher import Hasher
class MD5Hasher(Hasher):
    def Hashing(self,filePath:str)->str:
        m = hashlib.md5()
        with open(filePath) as fobj:
            while True:
                data = fobj.read(4096)
                if not data:
                    break
                m.update(data.encode('utf-8'))
        return m.hexdigest()