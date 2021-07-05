from pprint import pprint
import googlemaps 


API_KEY = 'AIzaSyC68QBAwtNlaneOx3L7kf_irbnb_ZNOzLg'

map_client = googlemaps.Client(API_KEY)

work_place_address= '1 Market St, San Francisco, CA'
response = map_client.geocode(work_place_address)
pprint(response)
print(response[0]['geometry'])