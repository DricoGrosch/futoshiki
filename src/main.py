import copy
import datetime

from src.agent import Agent
from src.environment import Environment
from src.lbs_agent import LBSAgent
from src.node import Node
from src.tile import Tile
totalViolations = 0
for _i in range(1, 2):
    env = None
    agent = None
    env = None
    winning_env = None
    # for i in range(30):
    env = Environment(game_number=20)
    #env.print_matrix()
    agent = Agent(env)
    # agent = LBSAgent(env)
    winning_board = None
    start = datetime.datetime.now()
    winning_env=None
    print('----------------')
    for number in env.get_available_numbers_to_throw(0, 0):
        _env = copy.deepcopy(env)
        # _env.print_matrix()
        _env.board[0][0] = Tile(number, env.board[0][0].restictions)
        agent.graph.current_node = Node(_env, 0, 0)
        winning_env = agent.build_winning_board()
        if winning_env:
            break
    end = datetime.datetime.now()
    # winning_env.print_matrix()
    totalViolations+=winning_env.violations
    # print((end - start).total_seconds())
    # print("---------------------------------------------------------------")
    # print("---------------------------------------------------------------")

print ("JOGO "+str(_i)+" violações"+ str(totalViolations/30))
totalViolations = 0
print("---------------------------------------------------------------")
