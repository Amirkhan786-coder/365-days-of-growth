# Q15. Create a new folder.

import os

folder_name = "practice_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created successfully.")
else:
    print("Folder already exists.")