import os
import os.path
import sys
rootdir = sys.argv[1]
file_object = open('resultList.txt','w')
for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        print(filename)
        print(parent)
        print(dirnames)
        file_object.write(parent+'/'+filename+'\n')
file_object.close()
