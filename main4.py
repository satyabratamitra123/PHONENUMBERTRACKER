import phonenumbers
import opencage
import os

from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
print("*************** starting ********************************************"

)
print(
    '//////////////////////////////////////////////////////////////////////////////////////////////////////////////'
    '//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
    'starting'
    '[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[['
    ';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')
target_number = input("DO YOU WANT TO FIND LOCATIONS OD MOBILE(YES/NO/DONT TRACK ):")
if target_number == 'yes':
    target = input("ENTER THE TARGET NUMBER WITH COUNTRY COD :")
    c_h = phonenumbers.parse(target, "CH")
    locations = (geocoder.description_for_number(c_h, 'en'))
    print(locations)
    print(timezone.time_zones_for_number(c_h))
    service_provider = phonenumbers.parse(target, "RO")
    print(carrier.name_for_number(service_provider, "en"))
    print("THIS TOOL IS UNDER WORKING")
elif target_number == "no":
    print("OK CLOSSING ")
elif target_number == "DONT TRACK":
    os.sysconf(__file__)
else:
    print("INVALID OPTIONS")
