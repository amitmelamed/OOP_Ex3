from src.GeoLocation import GeoLocation

class Node:
    id=0
    geoLocation=GeoLocation(0,0,0)

    def __init__(self,id,geoLocation):
        self.id=id
        self.geoLocation=geoLocation
