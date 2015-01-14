import googlemaps as GoogleMaps

from pygeocoder import Geocoder


results = Geocoder.geocode("Tian'anmen,Beijing")

print(results[0].coordinates)

