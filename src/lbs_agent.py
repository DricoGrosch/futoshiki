import copy
import datetime
import random

from src.agent import Agent


class LBSAgent(Agent):

    def __init__(self, *args, **kwargs):
        self.best_boards = []
        self.envs = []
        self.k = 4
        super(LBSAgent, self).__init__(*args, **kwargs)
        for i in range(self.k):
            _env = copy.deepcopy(self.env)
            _env.randomize_board()
            self.envs.append(_env)

    def build_winning_board(self):
        start = datetime.datetime.now()
        lost = False
        winner_env = None
        while (not lost and not winner_env):
            # lost = (datetime.datetime.now() - start).total_seconds() > 20
            child_envs = []
            print('-------------filhos----------')
            for env in self.envs:
                for row_index, row in enumerate(env.board):
                    for column_index, column in enumerate(row):
                        if not env.board[row_index][column_index].default:
                            for number in range(1, env.dimension):
                                _env = copy.deepcopy(env)
                                _env.board[row_index][column_index].number = number
                                # _env.print_matrix()
                                _env.refresh_violations(row_index,column_index)
                                print(_env.violations)
                                child_envs.append(_env)
            best_envs = list(sorted([*child_envs,*self.envs], key=lambda env: env.violations, ))[0:self.k]
            self.envs = best_envs
            for env in self.envs:
                if not env.violations:
                    return env.board
        return None
