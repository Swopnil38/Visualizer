import re
import numpy as np
import pandas as pd
import pycountry
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


list_alpha_2 = [i.alpha_2 for i in list(pycountry.countries)]
list_alpha_3 = [i.alpha_3 for i in list(pycountry.countries)]    

def country_flag(df):
    if (len(df)==2 and df in list_alpha_2):
        return pycountry.countries.get(alpha_2=df).name
    elif (len(df)==3 and df in list_alpha_3):
        return pycountry.countries.get(alpha_3=df).name
    else:
        return 'Invalid Code'
    
geolocator = Nominatim(user_agent='your unique UA')
def geolocate(country):
    try:
        # Geolocate the center of the country
        loc = geolocator.geocode(country)
        # And return latitude and longitude
        return [loc.latitude, loc.longitude]
    except GeocoderTimedOut:
        # Return missing value
        return geolocate(country)
    except:
        return 0,0
    
def update(name):
    data = pd.ExcelFile('data/{}.xlsx'.format(name))
    
    Geography = pd.read_excel(data,'Geography')
    country_name = []
    for i in Geography['Country']:
        country_ = country_flag(i)
        country_name.append(country_)
    Geography['Country_Name'] = country_name
    country_lat = []
    country_lon = []
    
    
    for i in Geography['Country']:
        countrys_lat,countrys_long = geolocate(i)
        country_lat.append(countrys_lat)
        country_lon.append(countrys_long)
    Geography['Latitude'] = country_lat
    Geography['Longitude'] = country_lon
   

    
    

    
    print("11")
    
    Geography.to_excel('try1.xlsx'.format(name), sheet_name='Geography')
    print("12")



    
update("Wedding Dreams")