import requests 
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

for home in homes:
    # get response
    r_work = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key)
    r_school = requests.get(url + "origins=" + home + "&destinations=" + school + "&key=" + api_key)

    # return time as text and as seconds 
    time_work = r_work.json()["rows"][0]["elements"][0]["duration"]["text"]
    time_school = r_school.json()["rows"][0]["elements"][0]["duration"]["text"]

    # seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

    # print the total travel time 
    print("Time from", home, "to")
    print("work:", time_work)
    print("school:", time_school, "\n")
    
    # print("Time from", home, "to school is", time_school, "\n")