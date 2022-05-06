import requests 
import csv
from datetime import date, datetime 
# import smtplib 

# API key 
# distance matrix api
api_file = open("api-key.txt", "r")
api_key = api_file.read()
api_file.close() 

# home address
# home = input("Enter a home address\n")
homes = []
# homes.append("Malden, MA")
# homes.append("Boston, MA")
homes.append("37 Rockwell St, Malden, MA 02148")
homes.append("1 Hummingbird Ln, Boston, MA 02126")

# work address 
# work = input("Enter a work address\n")
work = "640 Memorial Dr, Cambridge, MA 02139"

# school address
school = "360 Huntington Ave, Boston, MA 02115"

# base url 
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

fieldanmes = ['start', 'dest', 'date', 'start_time', 'travel_time']
date = date.today().strftime("%m/%d/%Y")    #current time
start_time = datetime.now().strftime("%H:%M")   #start time

# write to csv
with open('commute_time.csv', mode='a') as csv_file:
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
        
        '''
        # print the total travel time 
        print("Time from", home, "to")
        print("work:", time_work)
        print("school:", time_school, "\n")
        ''' 