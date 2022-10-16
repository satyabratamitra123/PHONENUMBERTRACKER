print("""       
   _ (`-. ('-. .-.                .-') _  ('-.         .-') _  _  .-')    ('-.   .-. .-')             .-') _            
  ( (OO  ( OO )  /               ( OO ) _(  OO)       (  OO) )( \( -O )  ( OO ).-\  ( OO )           ( OO ) )           
 _.`     ,--. ,--..-'),-----.,--./ ,--,(,------.      /     '._,------.  / . --. ,--. ,--. ,-.-'),--./ ,--,' ,----.     
(__...--'|  | |  ( OO'  .-.  |   \ |  |\|  .---'      |'--...__|   /`. ' | \-.  \|  .'   / |  |OO|   \ |  |\'  .-./-')  
 |  /  | |   .|  /   |  | |  |    \|  | |  |          '--.  .--|  /  | .-'-'  |  |      /, |  |  |    \|  | |  |_( O- ) 
 |  |_.' |       \_) |  |\|  |  .     |(|  '--.          |  |  |  |_.' |\| |_.'  |     ' _)|  |(_|  .     |/|  | .--, \ 
 |  .___.|  .-.  | \ |  | |  |  |\    | |  .--'          |  |  |  .  '.' |  .-.  |  .   \ ,|  |_.|  |\    |(|  | '. (_/ 
 |  |    |  | |  |  `'  '-'  |  | \   | |  `---.         |  |  |  |\  \  |  | |  |  |\   (_|  |  |  | \   | |  '--'  |  
 `--'    `--' `--'    `-----'`--'  `--' `------'         `--'  `--' '--' `--' `--`--' '--' `--'  `--'  `--'  `------'   

created by Satyabrata MItra

Version: 1.0.0

all rights reserved. Satyabrata Mitra


""")
import argparse
from unittest import result


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
result_s = geocoder.geocode(qeari)
lat = result_s[0] ["geometry"]["lat"]
lng = result_s[0] ["geometry"]["lng"]
print("THIS IS YOUR TARGET LATITUDE AND LONGITUD:"+ str(lat), lng)
FIDBACK = input("HOW WAS THE TOOLS (GOOD/BAD): ")
if FIDBACK == "GOOD":
    print("THANK YOU ")

elif FIDBACK == "BAD":
    print('OK SIR/MAM ')
else:
    print("WHY")

    
print("thanks for your feedback")

