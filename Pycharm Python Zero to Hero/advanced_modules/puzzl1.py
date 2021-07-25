import os
import shutil
import re

print(os.getcwd())
path = "C:\\Users\\ADMIN\\Desktop\\Complete-Python-3-Bootcamp-master\\12-Advanced Python Modules\\08-Advanced-Python-Module-Exercise\\unzip_me_for_instructions.zip"
#shutil.unpack_archive(path, os.getcwd(), "zip")
with open("extracted_content\\Instructions.txt") as f:
    for line in f.readlines():
        print(line)
for folder, sub_folders, files in os.walk(os.getcwd()+"\\extracted_content"):
    #print("Folder: ", folder)
    for sub_folder in sub_folders:
        #print("@Sub_folder: ", sub_folder)
        pass
    for file in files:
        #print(folder +  "\\" + file)
        with open(folder +  "\\" + file) as f:
            for line in f.readlines():
                pattern = r"\d{3}-\d{3}-\d{4}"
                result = re.search(pattern, line)
                try:
                    print(result.group())
                except:
                    continue
# Answer is 719-266-2837
