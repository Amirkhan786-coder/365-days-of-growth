# Q14. Display files and folders.

import os

items = os.listdir()

print("Files and Folders:")

for item in items:
    print(item)