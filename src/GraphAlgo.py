from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
import json


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g=DiGraph()):
        self.graph = g

    def load_from_json(self, file_name: str) -> bool:
        try:
            f = open(file_name)
            data = json.load(f)
            nodesArray = data["Nodes"]
            edgesArray = data["Edges"]
            for node in nodesArray:
                self.graph.add_node(node["id"])
            for edge in edgesArray:
                self.graph.add_edge(edge["src"], edge["dest"], edge["w"])
            return True
        except:
            print("file name wrong")
            return False

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        newList = [1, 2]
        return newList

    def plot_graph(self) -> None:
        pass

    def get_graph(self) -> GraphInterface:
        return self.graph

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass
