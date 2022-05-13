import pandas as pd
import glob
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Main file path where all digital agent folders are located ( in this case, 3rd party links)
Mainfile_path = filedialog.askopenfilename()


# File path for the 4 subfiles 
file_path1 = Mainfile_path + "\3rdPartyLinksReport\DigitalAgent.com"
file_path2 = Mainfile_path + "\3rdPartyLinksReport\DigitalAgent.ca"
file_path3 = Mainfile_path + "\3rdPartyLinksReport\DigitalAgent.net"
file_path4 = Mainfile_path + "\3rdPartyLinksReport\DigitalAgent.org"

# Array of all file paths
file_paths = [file_path1,file_path2,file_path3,file_path4]

# Getting all the files from their respective folders and putting it into one variable. There are 
# 20 different combined files, so we will use 20 variables to hold all the files from each respective folder

#blogAudit files

for x in file_paths:
    all_file_BlogAudit = glob.glob(x + "BlogAudit.sql" + "/*.csv")

li = []

for filename in all_file_BlogAudit:
    df = pd.read_csv(filename, index_col = None, header = 0 )
    li.append(df)






