# read the csv file 
import csv
from pathlib import Path 
dir = Path.cwd("C:\Users\User\Downloads\pfb group assignment_group 3 (4)\pfb group assignment_group 3")
csvdir = Path.cwd("C:\Users\User\Downloads\pfb group assignment_group 3 (4)\pfb group assignment_group 3")

def overheads_function(exchangerate):
    """
    This function will find the category with the highest value and return it in the txt file
    """
    overheads = {}
    with open(f"{csvdir}/Overheads.csv", newline='') as csvfile:
        # reads the csv file
        data = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(data):
            if i == 0:
                continue
            overheads.update({row[0]:row[1]})

    for key in overheads:
        try:
            overheads[key] = float(overheads[key])
            # converts all the values from strings to floats
        except:
            pass
 
    keylist = list(overheads.keys())
    vallist = list(overheads.values())
    position = vallist.index(max(overheads.values()))
    # this will find the category with the highest value

    with open(f"{dir}/summary_report.txt", 'a') as txtwriter:
        # this puts the category with the highest value in SGD into the txt file after multiplying the exchange rate
        txtwriter.write(f'[HIGHEST OVERHEADS] {keylist[position].upper()}, SGD{float(vallist[position]* exchangerate):.2f}\n')
    
# overheads_function()