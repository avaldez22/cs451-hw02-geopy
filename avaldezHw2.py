from geopy.geocoders import Nominatim

# Create a geolocator object to access geo data using Nominatum
geolocator = Nominatim()

# A query address
query = '1314 chavez st, las vegas, nm'

# Build/retrieve a geopy Location object with a query address
location = geolocator.geocode(query)

# Access the latitude from location object
print(location.latitude)

# Access the longitude from location object
print(location.longitude)

# View the Location object API
help(location)

#Can we compute distance between to geographic locations (using geodisic measurement)? Sure!

from geopy.distance import distance

#Location A

q = '1314 chavez st, las vegas, nm'

a = geolocator.geocode(q)


#Location B

q = '1701 bryant st, denver, co'

b = geolocator.geocode(q)


#Derive a latitude, longitude tuple for each location

aloc = (a.latitude, a.longitude)

bloc = (b.latitude, b.longitude)

#Compute distance in miles

d = distance(aloc, bloc).miles

print('distance', d)
