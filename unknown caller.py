import phonenumbers
from phonenumbers import timezone, geocoder, carrier

phoneNumber = phonenumbers.parse("+2347051242451")

timeZone = timezone.time_zones_for_number(phoneNumber)

Carrier = carrier.name_for_number(phoneNumber, 'en')

Region = geocoder.description_for_number(phoneNumber, 'en')

print(phoneNumber)
print(timeZone)
print(Carrier)
print(Region)
#Writen by Emmanuel Dalyop