# pip install googlemaps   ó conda install googlemaps
# pip install pandas
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyCGnoaDR2rZfvCQxMjUgAu14krTPWqmZs0') #'YOUR_API_KEY'


# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

for g in geocode_result:
  print(g.keys())
# result:
# dict_keys(['address_components', 'formatted_address', 'geometry', 'place_id', 'types'])  




# Look up an address with reverse geocoding
print("\n\n")

reverse_geocode = gmaps.reverse_geocode((37.4223878, -122.0841877))

for g in reverse_geocode:
  print(g.keys())
# result:
# dict_keys(['address_components', 'formatted_address', 'geometry', 'place_id', 'plus_code', 'types'])
# dict_keys(['address_components', 'formatted_address', 'geometry', 'place_id', 'types'])
# dict_keys(['address_components', 'formatted_address', 'geometry', 'place_id', 'plus_code', 'types'])
# dict_keys(['address_components', 'formatted_address', 'geometry', 'place_id', 'plus_code', 'types'])
# dict_keys(['address_components', 'formatted_address', 'geometry', 'place_id', 'types'])
# dict_keys(['address_components', 'formatted_address', 'geometry', 'place_id', 'types'])
# dict_keys(['address_components', 'formatted_address', 'geometry', 'place_id', 'types'])
# dict_keys(['address_components', 'formatted_address', 'geometry', 'place_id', 'types'])
# dict_keys(['address_components', 'formatted_address', 'geometry', 'place_id', 'types'])
# dict_keys(['address_components', 'formatted_address', 'geometry', 'place_id', 'types'])

