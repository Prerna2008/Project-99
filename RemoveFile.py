from genericpath import exists
import time
import os 
import shutil
path=input('Enter the name of the directory to be sorted:- ')
path1='c:/User/user/OneDrive/Desktop/Recycle Bin'
list_of_file=os.listdir(path)

if os.path.exists(path):
    shutil.move(path,path1)
else:
    os.makedirs(path)
    shutil.move(path,path1)

days=time.time()
isExist=os.path.exists(path)
print('It exists', isExist)
print(days)