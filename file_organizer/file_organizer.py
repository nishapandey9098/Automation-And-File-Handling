import os
import shutil

path = input("Enter the path of the directory to organize: "    )
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]  # Remove the dot from the extension
    
    if os.path.exists(path+'/' + extension):
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    else:
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
        