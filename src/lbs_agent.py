import copy
import datetime
import random

from src.agent import Agent


class LBSAgent(Agent):

    def __init__(self, *args, **kwargs):
        self.best_boards = []
        self.envs = []
        self.k =20
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

        while (not lost and not winner_env):
            # lost = (datetime.datetime.now() - start).total_seconds() > 60
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
            best_envs=[]
            idx=0
            for env in sorted_envs:
                if idx==self.k:
                    break
                if not best_envs:
                    best_envs.append(env)
                    idx+=1
                else:
                    board_duplicated = False
                    for _env in best_envs:
                        if env.board_to_str()==_env.board_to_str():
                            board_duplicated=True
                            break
                    if not board_duplicated:
                        best_envs.append(env)
                        idx += 1

            # best_envs=sorted_envs[0:self.k-1]
            # best_envs.append(sorted_envs[-1])
            self.envs = best_envs
            for env in best_envs:
                print(env.violations)
                if env.violations == 4:
                    env.print_matrix()
            for env in self.envs:
                if not env.violations:
                    return env.board
        return None
