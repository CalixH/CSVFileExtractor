import pandas as pd #panda is an excel manager for python
import glob #glob is a filepath manager
from tkinter import Tk, filedialog # tkinter is for file selection popup dialogues

pd.set_option('display.max_rows', None)

root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.
root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

# Main file path where all digital agent folders are located
Mainfile_path = filedialog.askdirectory()


# File path for the 4 subfiles 
file_path1 = Mainfile_path + "/DigitalAgent.com"
file_path2 = Mainfile_path + "/DigitalAgent.ca"
file_path3 = Mainfile_path + "/DigitalAgent.net"
file_path4 = Mainfile_path + "/DigitalAgent.org"

# Array of all file paths
file_paths = [file_path1,file_path2,file_path3,file_path4]
file_names = ["BlogAudit.sql.csv", "ComplianceQueueAudit.sql.csv", "ContentAudit.sql.csv", "DirectoryAudit.sql.csv", "DisclosureAudit.sql.csv", "EventAudit.sql.csv", "FileAudit.sql.csv", "OfficeVersionAudit.sql.csv", "OptionsAudit.sql.csv", "OrganizationalGroupAudit.sql.csv", "PageAudit.sql.csv", "ProfileAudit.sql.csv", "RepositoryAudit.sql.csv", "ResourceAudit.sql.csv", "SettingsAudit.sql.csv", "SubmissionFormVersionAudit.sql.csv", "TenantAudit.sql.csv", "UserAudit.sql.csv", "WebsiteAudit.sql.csv"]

# Getting all the files from their respective folders and putting it into one variable. There are 
# 20 different combined files, so we will use 20 variables to hold all the files from each respective folder

#blogAudit files

all_file_BlogAudit = []

for num,file in enumerate(file_paths):
    all_file_BlogAudit += glob.glob(file_paths[num] + file_names [0])

BlogAuditList = []

for filename in all_file_BlogAudit:
    df_BlogAudit = pd.read_csv(filename, index_col = None, header = 0 )
    BlogAuditList.append(df_BlogAudit)

#takes all the data and prints it on a new file called file.txt
with open("file.xls", "w") as output:
    output.write(str(BlogAuditList))
#####################################################################################






