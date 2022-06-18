import copy
import random

from src.node import Node
from src.tile import Tile


class Environment:

    def number_is_in_row(self, number, row):
        for tile in self.board[row]:
            if tile.number == number:
                return True
        return False

    def number_is_in_column(self, number, column):
        for row in self.board:
            if row[column].number == number:
                return True
        return False

    def print_matrix(self):
        str_board = ''
        for row in self.board:
            line = ' '.join([str(tile.number) for tile in row])
            str_board += line + '\n'
        print(str_board)

    def can_add_number(self, number, column, row):
        number_is_in_column = self.number_is_in_column(number, column)
        number_is_in_row = self.number_is_in_row(number, row)
        return not number_is_in_row and not number_is_in_column

    def get_available_numbers_to_throw(self, row, column):
        if self.board[row][column].number > 0:
            return [self.board[row][column].number]
        available_numbers = []
        for number in range(1, self.dimension + 1):
            if self.can_add_number(number, column, row):
                available_numbers.append(number)
        return available_numbers

    def __init__(self, dimension=4, random_start=True):
        self.dimension = dimension
        self.board = []
        for i in range(dimension):
            self.board.append([Tile(0, []) for j in range(dimension)])

        if random_start:
            for i in range(dimension):
                number = int(random.randrange(1, dimension))
                column = int(random.randrange(0, dimension - 1))
                row = int(random.randrange(0, dimension - 1))
                if self.can_add_number(number, column, row) and self.board[row][column] == 0:
                    self.board[row][column].number = number
        else:
            self.board[0][0].number = 0
            self.board[0][1].number = 0
            self.board[0][3].number = 0
            self.board[1][0].number = 1
            self.board[1][3].number = 2
            self.board[2][1].number = 1
            self.board[2][3].number = 3

            # self.board[0][0] = 0
            # self.board[1][1] = 1
            # self.board[1][3] = 0
            # self.board[3][2] = 0
            # self.board[3][3] = 0

            # self.board[0][0] = 3
            # self.board[0][1] = 0
            # self.board[0][2] = 0
            # self.board[0][3] = 0
            # self.board[0][4] = 0
            # # self.board[0][5] 0
            #
            # self.board[1][0] = 0
            # self.board[1][1] = 0
            # self.board[1][2] = 0
            # self.board[1][3] = 0
            # self.board[1][4] = 0
            # # self.board[1][5] 0
            #
            # self.board[2][0] = 0
            # self.board[2][1] = 0
            # self.board[2][2] = 0
            # self.board[2][3] = 0
            # self.board[2][4] = 0
            # # self.board[2][5] 0
            #
            # self.board[3][0] = 0
            # self.board[3][1] = 0
            # self.board[3][2] = 0
            # self.board[3][3] = 0
            # self.board[3][4] = 0
            # # self.board[3][5] 0
            #
            # self.board[4][0] = 4
            # self.board[4][1] = 0
            # self.board[4][2] = 0
            # self.board[4][3] = 3
            # self.board[4][4] = 0
            # self.board[4][5] = 2

            # self.board[5][0] = 0
            # self.board[5][1] = 0
            # self.board[5][2] = 2
            # self.board[5][3] = 4
            # self.board[5][4] = 1
            # self.board[5][5] = 0

    def create_node(self, row, column, number):
        _env = copy.deepcopy(self)
        _env.board[row][column].number = number
        return Node(_env, row, column)
