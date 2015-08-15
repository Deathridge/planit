import urllib2
import json as m_json
from bs4 import BeautifulSoup
import re
from datetime import datetime
from geopy import *
import pytz, math

def scrapeflight(flightcode, date):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    g = geocoders.GoogleV3()
    query = flightcode.replace(" ", "")
    response = opener.open( 'http://www.flightradar24.com/data/flights/' + query ).read()

    page = BeautifulSoup(response,'html.parser')
    
    for link in page.find_all('tr'):
        info = link.get('data-date')
        if (info==date):
            Latfrom = link.get('data-lat-from')
            Lonfrom = link.get('data-lon-from')
            LatTo = link.get('data-lat-to')
            LonTo = link.get('data-lon-to')            
            DepartureLocation = str(link.get('data-name-from'))
            ArrivalLocation= str(link.get('data-name-to'))
            t=0
            for time in link.find_all('td', {"class":"toCenter"}):
                Time = str(time)
                Time = re.findall("\>(.*?)\<", Time)
                if (t==0):
                    FromTimezone = int(round(float(Lonfrom) * 24/360,0))                    
                    
                    DepartureTime = datetime.strptime(Time[0], "%H:%M")
                 
                    if(FromTimezone + DepartureTime.hour > 23):
                        timezd = (FromTimezone + DepartureTime.hour) -24
                    elif (FromTimezone + DepartureTime.hour < 0):
                        timezd = 0 - (FromTimezone + DepartureTime.hour)                   
                    else:
                        timezd = FromTimezone + DepartureTime.hour    
                    DepartureTime = DepartureTime.replace(hour = timezd,minute = DepartureTime.minute)
                elif (t==2):                    
                    ToTimezone = int(round(float(LonTo) * 24/360,0))                     
                    print ToTimezone
                    ArrivalTime = datetime.strptime(Time[0], "%H:%M")
                    
                    if(ToTimezone + ArrivalTime.hour > 23):
                        timeza = (ToTimezone + ArrivalTime.hour) -24
                    elif (ToTimezone + ArrivalTime.hour < 0):
                        timeza = 0 - (ToTimezone + ArrivalTime.hour)
                    else:
                        timeza = (ToTimezone + ArrivalTime.hour)
                    ArrivalTime = ArrivalTime.replace(hour = timeza,minute = ArrivalTime.minute)

                t=t+1

    if ('DepartureLocation' not in locals()):
        Statuscode = 0
        DepartureLocation = "Invalid"
        ArrivalLocation = "Invalid"
        DepartureTime = date.time.Now()
        ArrivalTime = date.time.Now()
    elif ('DepartureTime' not in locals()):
        Statuscode = 1
        DepartureTime = datetime.date.today()
        ArrivalTime = datetime.date.today()
    else:
        Statuscode = 2

    return [flightcode, date, DepartureLocation, ArrivalLocation, DepartureTime, ArrivalTime, Statuscode]




