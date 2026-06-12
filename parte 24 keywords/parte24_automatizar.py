# Keywords: if we want to read, modify, or process a txt file, first we need a file path

import os # import os module
# Create a constant using this pattern and add the txt file you want to use:
# We have three options
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "archivo.txt") # 1- use this if the file is in the same folder
# 2- if it is on the desktop, there are two ways:
DATA_SCREEN = os.path.join(os.path.expanduser("~"), "Desktop", "archivo.txt") # expanduser("~") points to the user profile and avoids hardcoding ImKen.
DATA_SCREEN = r"C:\Users\ImKen\Desktop\archivo.txt" # use raw string for the path
# 3- the same if it is in another folder:
DATA_SCREEN = "C:/Users/ImKen/Desktop/archivo.txt" # this also works without raw string; use / instead of \
    
with open(DATA_SCREEN, mode="r", encoding="utf-8") as archivo: # with open (mode=r means read) as the file object name
    contents = archivo.read() # store file contents in a variable
    print(contents) # print them