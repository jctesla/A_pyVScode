# pip install googlemaps   ó conda install googlemaps
# Para saber cuales son los Method, debes correr dir(gmaps), y ah debe aparecer el methodo.
# testeador de API KEY : https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=AIzaSyCGnoaDR2rZfvCQxMjUgAu14krTPWqmZs0
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyCGnoaDR2rZfvCQxMjUgAu14krTPWqmZs0')

# For example, to retrieve the places near a specific location, you can use the places_nearby()
# This will retrieve the places near my House cajeros de BCP en un radio de 15*1609 mtrs
location = (-12.10314034134701, -76.96199937666326)
search_string = 'Cajero BCP'
distance = 15 * 1_609.344
business_list = []
places = gmaps.places_nearby(
                              location = location,
                              keyword = search_string,
                              name= 'Cajero BCP',
                              radius = distance
)

#print(places['results'])

                              
# Convert the data to a Pandas DataFrame: Once you have the data, you can convert 
# it to a Pandas DataFrame using the json_normalize()
import pandas as pd
from pandas.io.json import json_normalize
data = json_normalize(places['results'])

# Write the data to a CSV file:
data.to_csv('cajeros_bcp.csv', index=False)

