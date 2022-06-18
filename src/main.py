import copy

from src.agent import Agent
from src.environment import Environment
from src.node import Node
from src.tile import Tile

env = Environment(random_start=False)
env.print_matrix()
agent = Agent(env)
winning_board = None
a=env.get_available_numbers_to_throw(0, 0)
for number in env.get_available_numbers_to_throw(0, 0):
    _env = copy.deepcopy(env)
    _env.board[0][0] = Tile(number,env.board[0][0].restictions)
    agent.graph.current_node = Node(_env, 0, 0, )
    winning_board = agent.build_winning_board()
    if winning_board:
        agent.env.board = winning_board
        break
agent.env.print_matrix()
