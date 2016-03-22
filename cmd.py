import sys;
import os;

def GetPathSize(strPath):
    if not os.path.exists(strPath):
        return 0;
    if os.path.isfile(strPath):
        return os.path.getsize(strPath);
    nTotalSize = 0;
    for strRoot, lsDir, lsFiles in os.walk(strPath):
       for strDir in lsDir:
            nTotalSize = nTotalSize + os.path.getsize(os.path.join(strRoot, strDir));

       for strFile in lsFiles:
            nTotalSize = nTotalSize + GetPathSize(os.path.join(strRoot, strFile));
    return nTotalSize;

def getFileList(p):
        p = str(p)
        if p=="":
              return [ ]
        p = p.replace( "/","\\")
        if p[-1] != "\\":
             p = p+"\\"
        a = os.listdir(p)
        b = [x for x in a if os.path.isdir(p + x)]
        return b
file=open('out.txt','w')
PATH = sys.argv[0][0:-6]
PATH = "C:\\MAts\\"      #for test
make = getFileList(PATH)
for em in make:
     nFileSize =round( GetPathSize(PATH+em)/1024.0/1024.0/1024.0,3)
     if not nFileSize == 0:
         print em
         print(str(nFileSize)+"G")
         file.write(em+":\n"+str(nFileSize)+"G\n",)
file.close()
# if __name__ == '__main__':
#     nFileSize = GetPathSize(sys.argv[1])
#     print(round(nFileSize/1024.0/1024.0/1024.0,3));