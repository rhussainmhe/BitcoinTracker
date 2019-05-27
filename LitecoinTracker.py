import requests
import json
import csv

apikey = 'edba71467eaf257e89e235c9c17e222c3e76142e975c4a9f95c8fcbdc38b54d6'
symbol = 'LTC'
timestampCurrent = 1558727791
timestampOneYearAgo = 1527191791
oneDay = 86400

#API Call
base_url = "https://min-api.cryptocompare.com/data/dayAvg"
payload = {'fsym' : symbol,
            'api_key' : apikey,
            'tsym' : 'USD',
            'toTs' : str(timestampCurrent)}

r = requests.get(url = base_url, params = payload)

time = r.json()

def get_time_slot_data(timestamp):
    r = requests.get(base_url, params={'fsym' : symbol,
                'tsym' : 'USD',
                'toTs' : str(timestampCurrent)})
    if r.status_code == 200:
        return r.json()

#Open CSV writer
#Find range, Loop through, and save every days results for one year
with open('litecoin.csv', 'wb') as out:
    headers_written = False
    writer = csv.writer(out)
    for timestamp in range(timestampCurrent, timestampOneYearAgo, -oneDay):
        daily_data = get_time_slot_data(timestamp)
        if not headers_written and daily_data:
            writer.writerow(daily_data['USD'].keys())
            headers_written = True
        if daily_data:
            for entry in daily_data:
                writer.writerow(entry.values())
