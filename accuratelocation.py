import phonenumbers
import folium
from target import number
from phonenumbers import geocoder
key = 'MY_KEY'    

theNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(theNumber, "en")

print(yourLocation)


#Other details

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query =str(yourLocation)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']

long = results[0]['geometry']['lng']

print(lat, long)


myMap = folium.Map(location =[lat, long], zoom_start= 0)

folium.Marker([lat , long], popup=  yourLocation).add_to(myMap)


#html save
myMap.save("myLoc.html")