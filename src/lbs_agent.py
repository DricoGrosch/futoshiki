import copy
import datetime
import random

from src.agent import Agent


class LBSAgent(Agent):

    def __init__(self, *args, **kwargs):
        self.best_boards = []
        self.envs = []
        self.k =4
        super(LBSAgent, self).__init__(*args, **kwargs)
        for i in range(self.k):
            _env = copy.deepcopy(self.env)
            _env.randomize_board()
            _env.refresh_violations()
            self.envs.append(_env)

    def build_winning_board(self):
        start = datetime.datetime.now()
        lost = False
        winner_env = None

        while (not lost):
            seconds =(datetime.datetime.now() - start).total_seconds()
            print(seconds)
            lost = seconds > 30
            child_envs = []
            for env in self.envs:
                for row_index, row in enumerate(env.board):
                    for column_index, column in enumerate(row):
                        if not env.board[row_index][column_index].default:
                            for number in range(1, env.dimension+1):
                                _env = copy.deepcopy(env)
                                _env.board[row_index][column_index].number = number
                                _env.refresh_violations()
                                # env.print_matrix()
                                # print(_env.violations)
                                child_envs.append(_env)

            random.shuffle(child_envs)
            sorted_envs = list(sorted(child_envs, key=lambda env: env.violations, ))
            best_envs=sorted_envs[0:self.k]
            self.envs = best_envs
            for env in self.envs:
                if not winner_env:
                    winner_env=env
                if env.violations < winner_env.violations:
                    winner_env=env
        return winner_env
