from random import randint
import glob
import os
import json

file = open("month_names.json")
data = json.load(file)

months = data['months']
short_months = data['short_months']
amount = 100
directory = "./files/"

for i in range(amount):
    file_name_parts = [
        "Excel",
        str(randint(1, 31)).rjust(2, "0"),
        randint(1, 12),
        str(randint(2020, 2022))
    ]

    rand = randint(0, 10)

    if(rand < 3):
        file_name_parts[2] = short_months[file_name_parts[2] - 1]
    elif(rand < 7):
        file_name_parts[2] = months[file_name_parts[2] - 1]
    else:
        file_name_parts[2] = str(file_name_parts[2]).rjust(2, "0")

    fullname = str.join("_", file_name_parts)
    f = open(directory + fullname + ".txt", "w")
    f.close()

print(amount, "files generated")