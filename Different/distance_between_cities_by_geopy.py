from geopy.distance import geodesic as GD


New_York = (40.7128, 74.0060)
Texas = (31.9686, 99.9018)

print(f"The distance between New York and Texas is: {GD(New_York, Texas).km}")
