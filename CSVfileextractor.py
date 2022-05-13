import pandas as pd
import glob
import tkinter as tk
from tkinter import filedialog

root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.
root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

# Main file path where all digital agent folders are located ( in this case, 3rd party links)
Mainfile_path = filedialog.askdirectory()

# File path for the 4 subfiles 
file_path1 = Mainfile_path + "/DigitalAgent.ca"
file_path2 = Mainfile_path + "/DigitalAgent.com"
file_path3 = Mainfile_path + "/DigitalAgent.net"
file_path4 = Mainfile_path + "/DigitalAgent.org"

print(file_path1)

# Array of all file paths
file_paths = [file_path1,file_path2,file_path3,file_path4]

# Getting all the files from their respective folders and putting it into one variable
all_file_BlogAudit = None

for x in file_paths:
    all_file_BlogAudit += glob.glob(x + "BlogAudit.sql" + "/*.csv")

print(all_file_BlogAudit[0])




