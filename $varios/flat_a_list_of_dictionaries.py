def flatten_list(lst):
    plana = []
    for i in lst:
        if isinstance(i, dict):
            for _, value in i.items():
                if isinstance(value, list):
                    plana.extend(flatten_list(value))
                else:
                    plana.append(value)
        elif isinstance(i, list):
            plana.extend(flatten_list(i))
        else:
            plana.append(i)
    return plana
  
L0 = [{'address_components': [{'long_name': 'Google Building 40', 'short_name': 'Google Building 40', 'types': ['premise']}, {'long_name': '1600', 'short_name': '1600', 'types': ['street_number']}, {'long_name': 'Amphitheatre Parkway', 'short_name': 'Amphitheatre Pkwy', 'types': ['route']}, {'long_name': 'Mountain View', 'short_name': 'Mountain View', 'types': ['locality', 'political']}, {'long_name': 'Santa Clara County', 'short_name': 'Santa Clara County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'California', 'short_name': 'CA', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, {'long_name': '94043', 'short_name': '94043', 'types': ['postal_code']}], 'formatted_address': 'Google Building 40, 1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA', 'geometry': {'bounds': {'northeast': {'lat': 37.4226618, 'lng': -122.0829302}, 'southwest': {'lat': 37.4220699, 'lng': -122.084958}}, 'location': {'lat': 37.4223878, 'lng': -122.0841877}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 37.4236304802915, 'lng': -122.0825951197085}, 'southwest': {'lat': 37.4209325197085, 'lng': -122.0852930802915}}}, 'place_id': 'ChIJj38IfwK6j4ARNcyPDnEGa9g', 'types': ['premise']}] 
# L1 = {'address_components': [{'long_name': 'Google Building 40', 'short_name': 'Google Building 40', 'types': ['premise']}, {'long_name': '1600', 'short_name': '1600', 'types': ['street_number']}, {'long_name': 'Amphitheatre Parkway', 'short_name': 'Amphitheatre Pkwy', 'types': ['route']}, {'long_name': 'Mountain View', 'short_name': 'Mountain View', 'types': ['locality', 'political']}, {'long_name': 'Santa Clara County', 'short_name': 'Santa Clara County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'California', 'short_name': 'CA', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, {'long_name': '94043', 'short_name': '94043', 'types': ['postal_code']}], 'formatted_address': 'Google Building 40, 1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA', 'geometry': {'bounds': {'northeast': {'lat': 37.4226618, 'lng': -122.0829302}, 'southwest': {'lat': 37.4220699, 'lng': -122.084958}}, 'location': {'lat': 37.4223878, 'lng': -122.0841877}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 37.4236304802915, 'lng': -122.0825951197085}, 'southwest': {'lat': 37.4209325197085, 'lng': -122.0852930802915}}}, 'place_id': 'ChIJj38IfwK6j4ARNcyPDnEGa9g', 'types': ['premise']} 
# L2 = {'address_components': [{'long_name': '1600', 'short_name': '1600', 'types': ['street_number']}, {'long_name': 'Amphitheatre Parkway', 'short_name': 'Amphitheatre Pkwy', 'types': ['route']}, {'long_name': 'Mountain View', 'short_name': 'Mountain View', 'types': ['locality', 'political']}, {'long_name': 'Santa Clara County', 'short_name': 'Santa Clara County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'California', 'short_name': 'CA', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, {'long_name': '94043', 'short_name': '94043', 'types': ['postal_code']}], 'formatted_address': '1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA', 'geometry': {'location': {'lat': 37.4220656, 'lng': -122.0840897}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 37.4234145802915, 'lng': -122.0827407197085}, 'southwest': {'lat': 37.4207166197085, 'lng': -122.0854386802915}}}, 'place_id': 'ChIJj61dQgK6j4AR4GeTYWZsKWw', 'plus_code': {'compound_code': 'CWC8+R9 Mountain View, CA, USA', 'global_code': '849VCWC8+R9'}, 'types': ['establishment', 'point_of_interest']} 
# L3 = {'address_components': [{'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}], 'formatted_address': 'United States', 'geometry': {'bounds': {'northeast': {'lat': 74.071038, 'lng': -66.885417}, 'southwest': {'lat': 18.7763, 'lng': 166.9999999}}, 'location': {'lat': 37.09024, 'lng': -95.712891}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 74.071038, 'lng': -66.885417}, 'southwest': {'lat': 18.7763, 'lng': 166.9999999}}}, 'place_id': 'ChIJCzYy5IS16lQRQrfeQ5K5Oxw', 'types': ['country', 'political']} 

for i in L0:
#    print(flatten_list(i))
    print(i.keys(),"\n\n")
    
# result: son los keys de c/elemento de la lista.
# ['address_components', 'formatted_address', 'geometry', 'place_id', 'types']

# puedo leer c/u

