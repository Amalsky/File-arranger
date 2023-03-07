import os
import  shutil

os.chdir('C:\\Users\\amals\\Downloads')#changing dir

exe = 'C:\\Users\\amals\\Downloads\\EXE'#Folderpath

dir_list =os.listdir()

for file in dir_list:
    if os.path.isfile(file):
        path = 'C:\\Users\\amals\\Downloads'+'\\'+file#filepath

        if path.endswith('exe'):
            shutil.move(path, exe)






