print("""       .__        __                 __   .__                
______ |  |__   _/  |_____________  |  | _|__| ____    ____  
\____ \|  |  \  \   __\_  __ \__  \ |  |/ /  |/    \  / ___\ 
|  |_> >   Y  \  |  |  |  | \// __ \|    <|  |   |  \/ /_/  >
|   __/|___|  /  |__|  |__|  (____  /__|_ \__|___|  /\___  / 
|__|        \/                    \/     \/       \//_____/  

created by Satyabrata MItra

Version: 1.0.0

all rights reserved. Satyabrata Mitra


""")
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, type=str,
    help='path to the input file')
    parser.add_argument('-o', '--output', required=True, type=str,
    help='path to the output file')
    args = parser.parse_args()

    # MAIN WORK

import os

import phonenumbers
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier, geocoder, timezone

target = input("ENTER THE TARGET NUMBER WITH COUNTRY COD :")
c_h = phonenumbers.parse(target, "CH")
locations = (geocoder.description_for_number(c_h, 'en'))
print("THIS IS YOUR TARGET COUNTRY:"+locations)
LO = timezone.time_zones_for_number(c_h)
print("THIS IS YOUR TARGET TIME ZONE:"+str(LO))
service_provider = phonenumbers.parse(target, "RO")
print("THIS IS YOUR TARGET SIM PROVIDER :"+carrier.name_for_number(service_provider, "en"))
key = 'bbbafb3514fd43229acc391a2b5477e1'
geocoder = OpenCageGeocode(key)
qeari = str(locations)
r = geocoder.geocode(qeari)
lat = r[0] ["geometry"]["lat"]
lng = r[0] ["geometry"]["lng"]
print("THIS IS YOUR TARGET LATITUDE AND LONGITUD:"+ str(lat), lng)
# created by satyabrata mitra

