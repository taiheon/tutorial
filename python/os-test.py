#-------------------filelist in a folder---------------
# from os import listdir
# from os.path import isfile, join
# mypath=".\\"
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]
# print(onlyfiles)
#------------------specific file list in a folder---------------
import glob
print(glob.glob("*.py"))

import os
for itm in os.environ:
    print(itm, ' = ',os.getenv(itm))

for x in os.listdir():
    if x.endswith('py'):
        print(x)