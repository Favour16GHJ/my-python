import os
# FileNotFoundError for try and except
if os.path.exists("hi.txt"):
    print("It exists")
    os.remove("hi.txt")
else:
    print("The file doesn't exist")

# This is to delete an empty folder
os.rmdir("henry")