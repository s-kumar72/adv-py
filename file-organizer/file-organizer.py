import os
import shutil

os.chdir('//Users//sadhanakumar//github//adv-py//file-organizer//test-file')
## File Organizer
##  def include( )
##  Advanced Concepts in Python
##  June 2020

#dictionary of file categories and file extensions
DIRECTORIES = {
    "Web": [".html5", ".html", ".htm", ".xhtml", ".css", ".webarchive", ".php",
            ".yaml"],
    "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".jfif", ".svg"],
    "Photoshop": [".psd"],
    "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx", ".csv"],
    "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "Plain Text": [".txt", ".in", ".out", ".key", ".md"],
    "PDF": [".pdf"],
    "Code": [".py", ".java", ".RData", ".Rhistory", ".cpp", ".o"],
    "Shortcuts": [".lnk", ".url"],
    "Configuration": [".ini", ".msi", ".apk", ".crdownload"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]

}

#The path of the directory to be sorted
#edit this to where you placed your test-file folder
path = '//Users//sadhanakumar//github//adv-py//file-organizer//test-file'

#Creates a list with the filenames in the directory
list_ = os.listdir(path)

#goes through every file in the directory
for file_ in list_:

    ##START CODING HERE
    # 1. Create variables name and ext and set them to the file_'s name and extention
    #If the extension variable is empty, moves onto the next iteration
    #Checks if there is no extension
    file_list = file_.split(".")
    name = file_list[0]
    if len(file_list) > 1:
        ext = "." + file_list[1]

        # 2. Loop through DIRECTORIES
        for key in DIRECTORIES:
            # 3. If the extension is in one of the lists
            if ext in DIRECTORIES[key]:
                # 4. Check if the key is a folder in the current directory already
                new_path = os.path.join(path, key)
                if os.path.exists(new_path):
                    # 5. If the key is already a folder in the directory,
                    shutil.move(os.path.join(path, file_), new_path)
                    # move the file into that directory using shutil.move

                    # 6. If the folder is not in the current directory already,
                    # create the folder
                else:
                    os.mkdir(new_path)
                    print(os.getcwd())
                    # 7. Move the file into that directory using shutil.move
                    shutil.move(os.path.join(path,file_), new_path)
        # 8. Else, continue to the next iteration
        else:
            continue
