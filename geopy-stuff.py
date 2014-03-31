from geopy import geocoders

g = geocoders.GoogleV3()

place, (lat, lng) = g.geocode("10900 Euclid Ave in Cleveland")


from geopy import distance

_, ne = g.geocode('Newport, RI')  
_, cl = g.geocode('Cleveland, OH')  
distance.distance(ne, cl).km
