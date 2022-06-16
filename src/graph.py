from src.environment import Environment
from src.node import Node


class Graph:
    visited_nodes=set()
    open_nodes=set()
    current_node=None

    def get_node_neighbors(self):
        if self.current_node.column==self.current_node.env.dimension-1 and self.current_node.row < self.current_node.env.dimension-1:
            starter_row=self.current_node.row+1
        else:
            starter_row = self.current_node.row
        for row_index in range(starter_row,self.current_node.env.dimension):
            stater_column = self.current_node.column+1 if self.current_node.column+1 < self.current_node.env.dimension else 0
            for column_index in range(stater_column,self.current_node.env.dimension):
                number=self.current_node.env.board[row_index][column_index]
                if number>0:
                    _env = Environment(self.current_node.env.dimension,False)
                    _env.board=self.current_node.env.board
                    _env.board[row_index][column_index]=number
                    return [Node(_env,row_index,column_index)]
                numbers_available_to_throw = []
                for number in range(1,self.current_node.env.dimension+1):
                    if self.current_node.env.can_add_number(number,column_index,row_index):
                        _env = Environment(self.current_node.env.dimension, False)
                        _env.board = self.current_node.env.board
                        _env.board[row_index][column_index] = number
                        numbers_available_to_throw.append(Node(_env,row_index,column_index))
                return numbers_available_to_throw



    def add_open_nodes(self, current_node_neighbors):
        for neighbor in current_node_neighbors:
            self.open_nodes.add(neighbor)

    def visit_node(self, next_node_to_visit):
        self.current_node=next_node_to_visit
