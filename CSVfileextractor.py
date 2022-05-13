import pandas as pd
import glob
# you can use your own files here, I'm just using this to test
df1 = pd.DataFrame({"header_1":[1,2,3,4],"header_2": [2,3,4,6]})
df2 = pd.DataFrame({"header_4":[1,2,3,4],"header_3": [2,3,4,5]})

globbed_files = [df1,df2] #creates a list of all csv files
print(globbed_files)
data = [] # pd.concat takes a list of dataframes as an argument
i=1 # use this to set the file name counter
for csv in globbed_files:
    frame = csv
    frame["File_Name"] = "File " + str(i) # File_Name values are set here
    data.append(frame)
    i+=1

bigframe = pd.concat(data, ignore_index=True, keys=globbed_files)
bigframe = bigframe.reindex(sorted(df.columns), axis=1) # this arranges your columns alphabetically
bigframe = bigframe[ [ col for col in bigframe.columns if col != 'File_Name' ] + ['File_Name'] ] # takes File_Name column to the end