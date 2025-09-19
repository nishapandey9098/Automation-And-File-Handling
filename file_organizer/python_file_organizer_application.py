import os
import pathlib
import shutil
fileFormat = {
    "Web" : [".html5", ".html", ".htm", ".xhtml"],
    
    "Picture" : [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png",
                 ".bpg", ".svg", ".heif", ".psd"],
    
    "Video" : [".avi", ".mkv", ".flv", ".wmv", ".mov", ".mp4", ".webm",
               ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    
    "Document": [".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf",
                 ".ods", ".odt", ".pwi", ".xns", ".xps", ",dotx", ".docm", ".dox",
                 ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx"],
    
    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                   ".dmg", ".rar", ".xar", ".zip"],
    
    "Audio" : [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", 
               "oga", ".raw", ".vox", ".wav", ".wma"],
        
}

fileTypes = list(fileFormat.keys())
fileFormats = list(fileFormat.values())

print(fileFormats)
print(fileTypes)

downloads_path = r"C:\Users\Nisha\Downloads"
for file in os.scandir(downloads_path):
    fileName = pathlib.Path(file)
    fileFormatType = fileName.suffix.lower()
    
   # print(fileName)
   
    src = str(fileName)
    dest = "Other" 
    if fileFormatType == "":
        print(f" {src} has not file format")
    else:
        for formats in fileFormats:
            if fileFormatType in formats:
                folder = fileTypes[fileFormats.index(formats)]
                print(folder)
                if os.path.isdir(folder) == False:
                    os.mkdir(folder)
                dest = folder
        else:
            if os.path.isdir("Other") == False:
             os.mkdir("Other")  
             
    print(src, "moved to ", dest, " ! ") 
    shutil.move(src, dest)
    
print("File Organizer Started")
input("\n Press enter to EXIT")
    
    
    