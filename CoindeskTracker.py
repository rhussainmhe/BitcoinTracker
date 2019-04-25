import requests
import json
import csv

start = '2018-04-23'
end = '2019-04-23'

base_url = ("https://api.coindesk.com/v1/bpi/historical/close.json" + "?start=" + start + "&end=" + end)

r = requests.get(url = base_url)

fullyear = r.json()
print('Printing base_url')
print(base_url)

print('printing fullyear')
print(fullyear)

#write csv file with bpi items

with open('/Users/riaz_hussain/Desktop/Code/Python/BitcoinTracker/bitcoinyear.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in fullyear['bpi'].items():
        writer.writerow([key,value])
