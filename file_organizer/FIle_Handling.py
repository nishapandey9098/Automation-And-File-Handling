# file handling: navigate, rename, move, copy, remove
#how to keep your desktop organized

import os
from pathlib import Path
import shutil

os.chdir('/Users/Nisha/Documents/UPWORK/Ui_designs')

#os.remove("filename")
#os.rmdir("data")
shutil.rmtree("data")

#print(os.getcwd())

#print(os.listdir())

#Path("data").mkdir(exist_ok=True)
#if not os.path.exists("data"):
#   os.mkdir("data")
    
#for file in os.listdir():
#   print(file)
#    if file == '.DS_Store':
#   if file == '.DS_Store' or file == "data":
#      continue
#    shutil.move(file,"data")
#    shutil.copy2(file,"data") #same timestamp as copy1
#    print(file)
#    name, ext = os.path.splitext(file)
#    print(name)
#    print(ext)

#    f = Path(file)
#    name, ext = f.stem, f.suffix
#   splitted = name.split("-")
#   print (splitted)
#    splitted = [s.strip() for s in splitted]
#   new_name = f"{splitted[0]}{ext}"
#    print(new_name)
#    os.rename(file, new_name)
#   f.rename(new_name)
    
    