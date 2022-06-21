import copy
import datetime

from src.agent import Agent
from src.environment import Environment
from src.lbs_agent import LBSAgent
from src.node import Node
from src.tile import Tile

env = Environment(game_number=3, dimension=6)
env.print_matrix()
# agent = Agent(env)
agent = LBSAgent(env)
winning_board = None
start = datetime.datetime.now()
for number in env.get_available_numbers_to_throw(0, 0):
    _env = copy.deepcopy(env)
    _env.board[0][0] = Tile(number, env.board[0][0].restictions)
    agent.graph.current_node = Node(_env, 0, 0)
    winning_board = agent.build_winning_board()
    if winning_board:
        agent.env.board = winning_board
        break
end = datetime.datetime.now()
agent.env.print_matrix()
print((end - start).total_seconds())
