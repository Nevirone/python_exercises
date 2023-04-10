from glob import glob
import time
import os
import json

file = open("month_names.json")
data = json.load(file)

months = data['months']
short_months = data['short_months']

files_directory = "./files/*.txt"
files = glob(files_directory)

for file in files:
    old_title = file
    words = file.split(sep="_")

    for i in range(12):
        if words[2] == months[i] or words[2] == short_months[i]:
            words[2] = str(i+1).rjust(2, "0")
            break

    new_title = str.join("_", words)

    if(old_title == new_title):
        continue

    
    if(os.path.isfile(new_title)):
        print("File of that name already exists, skipping")
        continue

    os.rename(old_title, new_title)
    print("Renamed", old_title.split("\\")[1], "to", new_title.split("\\")[1])

    time.sleep(0.05)






