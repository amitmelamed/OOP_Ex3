from src.GeoLocation import GeoLocation


class Node:

    def __init__(self, id : int, pos: tuple = None):
        self.id = id
        self.geoLocation = pos
        self.inEdges={}
        self.outEdges={}


