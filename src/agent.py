from src.graph import Graph
from src.node import Node


class Agent:
    graph=None
    env = None

    def __init__(self,env,*args,**kwargs):
        self.graph=Graph()
        self.env=env
        self.graph.current_node=Node(self.env,0,0,)

    def build_winning_track(self):
        meta_node_found = False
        winning_track = []
        while(not meta_node_found):
            current_env=self.graph.current_node.env
            current_node_neighbors = self.graph.get_node_neighbors()
            self.graph.add_open_nodes(current_node_neighbors)
            next_node_to_visit = self.pop_from_open_nodes(self.graph.open_nodes)
            if next_node_to_visit:
                self.graph.visit_node(next_node_to_visit)

    def pop_from_open_nodes(self, open_nodes):
        return self.graph.open_nodes.pop()
