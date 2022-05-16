import pandas as pd #panda is an excel manager for python
import glob #glob is a filepath manager
from tkinter import Tk, filedialog # tkinter is for file selection popup dialogues
from openpyxl import load_workbook #excel read/writer
import os

pd.set_option('display.max_rows', None)

root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.
root.attributes('-topmost', True)
root.update()

# Main file path where all digital agent folders are located
Mainfile_path = filedialog.askdirectory()


# File path for the 4 subfiles 
file_path1 = Mainfile_path + "/DigitalAgent.com"
file_path2 = Mainfile_path + "/DigitalAgent.ca"
file_path3 = Mainfile_path + "/DigitalAgent.net"
file_path4 = Mainfile_path + "/DigitalAgent.org"

# Array of all file paths
file_paths = [file_path1,file_path2,file_path3,file_path4]
file_names = ["BlogAudit", "ComplianceQueueAudit", "ContentAudit", "DirectoryAudit", "DisclosureAudit", "EventAudit", "FileAudit", "OfficeVersionAudit", "OptionsAudit", "OrganizationalGroupAudit", "PageAudit", "ProfileAudit", "RepositoryAudit", "ResourceAudit", "SettingsAudit", "SubmissionFormVersionAudit", "TenantAudit", "UserAudit", "WebsiteAudit"]
file_tail = ".sql.csv"

# Getting all the files from their respective folders and putting it into one variable. There are 
# 20 different combined files, so we will use 20 variables to hold all the files from each respective folder

#blogAudit files
counter = 0

if os.path.isdir(Mainfile_path + "/Digital Agent Combined") == False:
    os.mkdir(Mainfile_path + "/Digital Agent Combined")

for name in file_names:
    all_file_BlogAudit = []

    for num,file in enumerate(file_paths):
        all_file_BlogAudit += glob.glob(file_paths[num] + "/" + file_names[counter] + file_tail)

    BlogAuditList = []

    for filename in all_file_BlogAudit:
        df_BlogAudit = pd.read_csv(filename, index_col = None, header = 0 )
        BlogAuditList.append(df_BlogAudit)

    df_BlogAudit = pd.concat(BlogAuditList, axis = 0, ignore_index = True)

    df_BlogAudit.to_excel(Mainfile_path + "/Digital Agent Combined/" + name + "Combined.xlsx", index=False)
    counter += 1






