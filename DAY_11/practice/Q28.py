# Question:
# Check whether a file exists.

import os

if os.path.exists("data.txt"):
    print("File Exists")
else:
    print("File Does Not Exist")