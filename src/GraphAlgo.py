from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):
    graph=DiGraph();
    def __init__(self,graph):
        self.graph=graph

    def __init__(self):
        self.graph=DiGraph()
    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass