import pandas as pd
import glob
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Main file path where all digital agent folders are located ( in this case, 3rd party links)
Absfile_path = filedialog.askopenfilename()
