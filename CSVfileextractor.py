import pandas as pd
import glob
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Main file path where all digital agent folders are located ( in this case, 3rd party links)
Mainfile_path = filedialog.askopenfilename()

# File path for the 4 subfiles in the 
file_path1 = Mainfile_path + "/DigitalAgent.ca"
file_path2 = Mainfile_path + "/DigitalAgent.com"
file_path3 = Mainfile_path + "/DigitalAgent.net"
file_path4 = Mainfile_path + "/DigitalAgent.org"
