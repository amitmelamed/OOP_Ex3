from src.GraphInterface import GraphInterface
from Node import Node
from Edge import Edge
from GeoLocation import GeoLocation


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.edgesCount = 0

    def v_size(self) -> int:
        return self.nodes.__sizeof__()

    def e_size(self) -> int:
        return len(self.edges)

    def get_mc(self) -> int:
        pass

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if (self.nodes.get(id1) == None or self.nodes.get(id2) == None):
            return False
        self.nodes[id1].outEdges[id2] = Edge(id1, id2, weight)
        self.nodes[id2].inEdges[id1] = Edge(id1, id2, weight)
        self.edges[self.edgesCount] = Edge(id1, id2, weight)
        self.edgesCount = self.edgesCount + 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        self.nodes[node_id] = Node(node_id, pos)
        return True

    def remove_node(self, node_id: int) -> bool:
        if (self.nodes.get(node_id) == None):
            return False
        self.nodes.pop(node_id)
        for key in self.edges:
            if(self.edges[key]!=None):
                if(self.edges[key].src==node_id or self.edges[key].dest==node_id ):
                    self.edges.pop(key)
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if(self.nodes[node_id1]==None or self.nodes[node_id2]==None):
            return False
        self.nodes[node_id1].outEdges.pop(node_id2)
        self.nodes[node_id2].inEdges.pop(node_id1)
        for key in self.edges:
            if(self.edges[key]!=None):
                if(self.edges[key].src==node_id1 and self.edges[key].dest==node_id2):
                    self.edges.pop(key)
                    break
        return True

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.nodes.get(id1).inEdges

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.nodes.get(id1).outEdges
