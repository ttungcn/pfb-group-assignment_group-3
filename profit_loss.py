import csv
from pathlib import Path
dir = Path("C:\Users\celeste tay\Downloads\pfb group assignment_group 3")
csvdir = Path("C:\Users\celeste tay\Downloads\pfb group assignment_group 3\csv reports")

def profitloss_function(exchangerate):
    """
    This function will read only the values from the profit & loss csv file and find the day where the amount of 
    net profit is lower than the previous day
    """
    profitloss = {}
    with open(f"{csvdir}/Profit & Loss.csv", newline='') as csvfile:
        # reads the csv file
            data = csv.reader(csvfile, delimiter=',')
            for i, row in enumerate(data):
                if i == 0:
                    continue
                # skips headers
                profitloss.update({row[0]:row[4]})

    for key in profitloss:
            try:
                profitloss[key] = float(profitloss[key])
            # converts all the values from strings to floats
            except:
                pass

    profitlosslist = list(profitloss.values())
    # puts only the profit and loss values into a list
    keylist = list(profitloss.keys())
    # puts the keys(days) into a list

    counter = 1
    with open(f"{dir}/summary_report.txt", 'a') as txtwriter:
        """
        This will upload the final information into the txt file after meeting the conditions
        """
        for i, number in enumerate(profitlosslist):
            if i == 0:
                previous = number
                # the first number does not have a previous number so it becomes the previous number
                continue
            if number < previous:
                # if the next day's net profit is lower than the previous day, the difference and its designated day
                # will be converted from USD to SGD and be returned into the txt file
                difference = previous - number
                txtwriter.write(f'[PROFIT DEFICIT] DAY: {keylist[i]}, AMOUNT: SGD{difference * exchangerate}\n')
            if number > previous:
                counter += 1 
                if counter == len(profitlosslist):
                    # if the counter goes through all the numbers and they are all higher than the previous day,
                    # it will be returned as a net profit surplus in the txt file
                    txtwriter.write(f'[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
            previous = number


# profitloss_function()