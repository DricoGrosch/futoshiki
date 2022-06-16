from src.graph import Graph
from src.node import Node


class Agent:
    graph=None
    env = None

    def __init__(self,env,*args,**kwargs):
        self.current_node = None
        self.graph=Graph()
        self.env=env

    def finish(self,env):
        has_empty_value = False
        for row in env.board:
            if 0 in row:
                has_empty_value = True

        if not has_empty_value:
            return True,True

        has_open_node = len(self.graph.open_nodes)>0
        if has_empty_value and not has_open_node:
            return True,False
        return False,False

    def build_winning_board(self):
        # print('MR HAN IS PLAYING. SILENCE, PLEASE...')
        finished = False
        winning_board=[]
        while(not finished):
            current_env=self.graph.current_node.env
            current_node_neighbors = self.graph.get_node_neighbors()
            self.graph.add_open_nodes(current_node_neighbors)
            finished, winner = self.finish(current_env)
            if finished:
                if winner:
                    winning_board = current_env.board
            next_node_to_visit = self.pop_from_open_nodes(self.graph.open_nodes)

            if next_node_to_visit:
                self.graph.visit_node(next_node_to_visit)
        return winning_board

    def pop_from_open_nodes(self, open_nodes):
        return self.graph.open_nodes.pop(0)
