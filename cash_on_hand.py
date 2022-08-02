import csv
from pathlib import Path
dir = Path("//Mac/Home/Documents/pfb group assignment_group 3")
csvdir = Path("//Mac/Home/Documents/pfb group assignment_group 3/csv reports")

cashonhand = {}
def coh_function(exchangerate):
    """
    This function will read only the values from the cash-on-hand csv file and find the day where the amount of 
    cash on hand is lower than the previous day
    """
    with open(f"{csvdir}/Cash-on-Hand.csv", newline='') as csvfile:
        # reads the csv file
            data = csv.reader(csvfile, delimiter=',')
            for i, row in enumerate(data):
                if i == 0:
                    continue
                # skip headers
                cashonhand.update({row[0]:row[1]})

    for key in cashonhand:
            try:
                cashonhand[key] = float(cashonhand[key])
                # converts all the values from strings to floats
            except:
                pass

    cashonhandlist = list(cashonhand.values())
    # puts only the cash on hand values into a list
    keylist = list(cashonhand.keys())
    # puts the keys (days) into a list

    counter = 1
    with open(f"{dir}/summary_report.txt", 'a') as txtwriter:
        """
        This will upload the final information into the txt file after meeting the conditions
        """
        for i, number in enumerate(cashonhandlist):
            if i == 0:
                previous = number
                # the first number does not have a previous number so it becomes the previous number
                continue
            if number < previous:
                # if the next day's cash on hand is lower than the previous day, the difference and its designated day
                # will be converted from USD to SGD and be returned into the txt file
                difference = previous - number
                txtwriter.write(f'[CASH DEFICIT] DAY: {keylist[i]}, AMOUNT: SGD{difference * exchangerate}\n')
            if number > previous:
                counter += 1
                if counter == len(cashonhandlist):
                    # if the counter goes through all the numbers and they are all higher than the previous day,
                    # it will be returned as a cash surplus in the txt file
                    txtwriter.write('[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
            previous = number
                

# coh_function()

