# api key: HKD184RX47343TZP
import requests 
from pathlib import Path 
dir = Path("//Mac/Home/Documents/pfb group assignment_group 3")

def api_function():
# replace the "demo" api key below with key from https://www.alphavantage.co/support/#api-key
    try:
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=HKD184RX47343TZP'
        r = requests.get(url)
        data = r.json()
        exchangerate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

        if exchangerate == None:
            raise ValueError

        with open(f"{dir}/summary_report.txt", 'a') as txtwriter:
            # puts the real time currency conversion rate into the summary report txt file
            txtwriter.write(f'[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{float(exchangerate):.5f}\n')

    except requests.exceptions.JSONDecodeError:
        """
        This will give an error if the website is not working and give a default exchange rate of USD to SGD
        """
        print("WEBSITE IS NOT VALID. USING DEFAULT EXCHANGE RATE USD1 = SGD1.36")
        exchangerate = 1.36
        
        with open(f"{dir}/summary_report.txt", 'a') as txtwriter:
            # puts the default currency conversion rate into the txt file
            txtwriter.write(f'[DEFAULT CURRENCY CONVERSION RATE] USD1 = SGD{float(exchangerate):.5f}\n')

    except ValueError:
        """
        This will give an error if the website returns a non-valid exchange rate and give a default 
        exchange rate of USD to SGD
        """
        print("NONETYPE NOT EXPECTED VALUE OF EXCHANGE RATE. USING DEFAULT EXCHANGE RATE USD1 =  SGD1.36")
        exchangerate = 1.36

        with open(f"{dir}/summary_report.txt", 'a') as txtwriter:
            # puts the default currency conversion rate into the txt file
            txtwriter.write(f'[DEFAULT CURRENCY CONVERSION RATE] USD1 = SGD{float(exchangerate):.5f}\n')

    return float(exchangerate)

# api_function()
