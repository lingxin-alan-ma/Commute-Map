import requests 
import csv
import json 
from datetime import date, datetime 

# API key 
# distance matrix api
api_file = open("api-key.txt", "r")
api_key = api_file.read()
api_file.close() 

# open address json file
f = open('address.json')
addr = json.load(f)

# home address
home = addr['home'] 

# work address 
work = addr['work'] 

# school address
school = addr['school'] 

# close json file
f.close()

# base url 
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

fieldanmes = ['start', 'dest', 'date', 'start_time', 'travel_time']
date = date.today().strftime("%m/%d/%Y")    #current time
start_time = datetime.now().strftime("%H:%M")   #start time

# write to csv
with open('commute_time_sample.csv', mode='a') as csv_file:
    # using | as delimiter as there are "," in address
    time_writer = csv.writer(csv_file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

    for home in homes:
        # get response
        r_work = requests.get(url + "origins=" + home + "&destinations=" + work + "&departure_time=now&key=" + api_key)
        r_school = requests.get(url + "origins=" + home + "&destinations=" + school + "&departure_time=now&key=" + api_key)
        # return time as text and as seconds 
        time_work = r_work.json()["rows"][0]["elements"][0]["duration_in_traffic"]["text"]
        time_school = r_school.json()["rows"][0]["elements"][0]["duration_in_traffic"]["text"]
        
        time_writer.writerow([home, work, date, start_time, time_work])
        time_writer.writerow([home, school, date, start_time, time_school])
       