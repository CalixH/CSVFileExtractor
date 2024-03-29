# install python libraries
import os
os.system("pip3 install pandas")
os.system("pip3 install openpyxl")
os.system("pip3 install xlsxwriter")

import pandas as pd #panda is an excel manager for python
import glob #glob is a filepath manager
from tkinter import Tk, filedialog # tkinter is for file selection popup dialogues
import sys # early termination
import xlsxwriter # allows to write to one excel file

# list containing all paths to folders with excel files
folder_paths = []

# This is a recursive function that finds the path to folders containing excel files
def getPath(Mainfile_path):
    for name in os.listdir(Mainfile_path): # ignore this file
        if name == ".DS_Store":
            continue
        if os.path.isfile(Mainfile_path + "/" + name): # if we've found a folder containing excel files, add it to the list and return
            folder_paths.append(Mainfile_path)
            return
        getPath(Mainfile_path + "/" + name) # else continue recursing

pd.set_option('display.max_rows', None)

root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.
root.attributes('-topmost', True)
root.update()

# Main file path where all digital agent folders are located
Mainfile_path = filedialog.askdirectory()
getPath(Mainfile_path)

# Checks whether you selected the right directory to merge files
if os.path.isdir(folder_paths[0]) == False:
    print("------- SCRIPT TERMINATED ---------")
    sys.exit("Wrong folder selected. Please see documentation for details")

# Array of all file paths
file_names = ["profile"]
file_tail = ".csv"

# add unique file names to our file name list
for path in folder_paths:
    for file in os.listdir(path):
        if file not in file_names and file != ".DS_Store":
            file_names.append(file)

counter = 0

# slice the .csv off of our file names
for name in file_names:
    file_names[counter] = name[0:len(name)-4]
    counter += 1

# Getting all the files from their respective folders and putting it into one variable. There are 
# different combined files, so we will loop through and create 19 combined files

# Manual counter for iterating through 19 files
counter = 0

# If Digital Agent Combined folder doesn't exist, make it exist
if os.path.isdir(Mainfile_path + "/Digital Agent Combined") == False:
    os.mkdir(Mainfile_path + "/Digital Agent Combined")

#Creates a single workbook in excel called AllAuditCombined
workbook = xlsxwriter.Workbook(Mainfile_path + "/Digital Agent Combined/AllAuditCombined.xlsx")

# List to store the 19 dataframes
listofconcatdf = []

# Creates an Excel writer to write to each sheet in the workbook
writer = pd.ExcelWriter(Mainfile_path + "/Digital Agent Combined/AllAuditCombined.xlsx", engine='xlsxwriter')

# loops through 19 times to combine and create 19 worksheets
for name in file_names:

    # List to store the 4 files with the same name, eg. BlogAudit
    all_files = []

    # Get all the files with same name under .com, .org, .ca, .net
    for num,file in enumerate(folder_paths):
        all_files += glob.glob(folder_paths[num] + "/" + file_names[counter] + file_tail)

    # List to store the dataframes for files with the same name
    dfList = []

     # Loops through all the files and makes a list with the 4 dataframes by appending it to dfList
    for filename in all_files:
        df = pd.read_csv(filename, index_col = None, header = 0 )
        dfList.append(df)

    # Concatenate the 4 dataframes in dfList to create 1 large dataframe which is easier to print in excel, and then append that to the global listofdf,
    # which should contain 19 combined files once the loop completes
    df = pd.concat(dfList, axis = 0, ignore_index = True)
    listofconcatdf.append(df)

    
    #increment counter to function for the next file in the filename array
    counter += 1

# Resets counter
counter = 0

# Loops through a second time to write all the listofdf into each respective excel sheet
for df in listofconcatdf:
  df.to_excel(writer, sheet_name= "All" + file_names[counter])
  counter +=1

# Saves the workbook
writer.save()






