import copy
import random

from src.node import Node
from src.tile import Tile


class Environment:
    def __init__(self, dimension=4, game_number=1):
        self.dimension = dimension
        self.board = []
        self.violations = 0
        for i in range(dimension):
            self.board.append([Tile(0, []) for j in range(dimension)])
        # easy
        if game_number == 1:
            self.board[0][0].number = 0
            self.board[0][1].number = 0
            self.board[0][2].number = 0
            self.board[0][3].number = 2
            self.board[0][3].default = True

            self.board[1][0].number = 0
            self.board[1][1].number = 0
            self.board[1][2].number = 0
            self.board[1][3].number = 0

            self.board[2][0].number = 0
            self.board[2][1].number = 0
            self.board[2][2].number = 0
            self.board[2][3].number = 0

            self.board[3][0].number = 0
            self.board[3][1].number = 0
            self.board[3][2].number = 0
            self.board[3][3].number = 0

            self.board[0][0].restictions = ['>']
            self.board[1][1].restictions = ['V']
            self.board[1][2].restictions = ['<', '^']
            self.board[2][2].restictions = ['<']
            self.board[3][1].restictions = ['>']
        # extreme
        elif game_number == 2:
            self.board[0][0].number = 0
            self.board[0][1].number = 0
            self.board[0][2].number = 0
            self.board[0][3].number = 0

            self.board[1][0].number = 0
            self.board[1][1].number = 0
            self.board[1][2].number = 0
            self.board[1][3].number = 0

            self.board[2][0].number = 0
            self.board[2][1].number = 0
            self.board[2][2].number = 0
            self.board[2][3].number = 0

            self.board[3][0].number = 1
            self.board[3][0].default = True
            self.board[3][1].number = 3
            self.board[3][1].default = True
            self.board[3][2].number = 0
            self.board[3][3].number = 0

            self.board[0][0].restictions = ['V']
            self.board[0][1].restictions = ['>']
            self.board[1][2].restictions = ['^']
            self.board[2][1].restictions = ['^']
            self.board[3][2].restictions = ['>']
        # extreme 6x6
        elif game_number == 3:
            self.board[0][0].number = 1
            self.board[0][0].default = True
            self.board[0][1].number = 0
            self.board[0][2].number = 0
            self.board[0][3].number = 0
            self.board[0][4].number = 0
            self.board[0][5].number = 0

            self.board[1][0].number = 0
            self.board[1][1].number = 0
            self.board[1][2].number = 0
            self.board[1][3].number = 0
            self.board[1][4].number = 0
            self.board[1][5].number = 0

            self.board[2][0].number = 0
            self.board[2][1].number = 0
            self.board[2][2].number = 0
            self.board[2][3].number = 0
            self.board[2][4].number = 0
            self.board[2][5].number = 0

            self.board[3][0].number = 0
            self.board[3][1].number = 0
            self.board[3][2].number = 0
            self.board[3][3].number = 0
            self.board[3][4].number = 0
            self.board[3][5].number = 2
            self.board[3][5].default = True

            self.board[4][0].number = 0
            self.board[4][1].number = 0
            self.board[4][2].number = 0
            self.board[4][3].number = 0
            self.board[4][4].number = 0
            self.board[4][5].number = 0

            self.board[5][0].number = 0
            self.board[5][1].number = 0
            self.board[5][2].number = 0
            self.board[5][3].number = 0
            self.board[5][4].number = 0
            self.board[5][5].number = 0

            self.board[0][1].restictions = ['V', '<']
            self.board[0][4].restictions = ['V']
            self.board[1][2].restictions = ['>', '^']
            self.board[1][3].restictions = ['>']
            self.board[1][4].restictions = ['>']
            self.board[2][0].restictions = ['V']
            self.board[3][0].restictions = ['<']
            self.board[3][3].restictions = ['<']
            self.board[4][4].restictions = ['^']
            self.board[5][0].restictions = ['<']
            self.board[5][4].restictions = ['<']
        # extreme 9x9
        elif game_number == 4:
            self.board[0][0].number = 0
            self.board[0][1].number = 0
            self.board[0][2].number = 0
            self.board[0][3].number = 6
            self.board[0][4].number = 0
            self.board[0][5].number = 0
            self.board[0][6].number = 8
            self.board[0][7].number = 9
            self.board[0][8].number = 5

            self.board[1][0].number = 0
            self.board[1][1].number = 4
            self.board[1][2].number = 0
            self.board[1][3].number = 1
            self.board[1][4].number = 0
            self.board[1][5].number = 0
            self.board[1][6].number = 5
            self.board[1][7].number = 2
            self.board[1][8].number = 0

            self.board[2][0].number = 0
            self.board[2][1].number = 1
            self.board[2][2].number = 0
            self.board[2][3].number = 0
            self.board[2][4].number = 6
            self.board[2][5].number = 7
            self.board[2][6].number = 4
            self.board[2][7].number = 0
            self.board[2][8].number = 3

            self.board[3][0].number = 0
            self.board[3][1].number = 0
            self.board[3][2].number = 0
            self.board[3][3].number = 3
            self.board[3][4].number = 0
            self.board[3][5].number = 0
            self.board[3][6].number = 0
            self.board[3][7].number = 0
            self.board[3][8].number = 0

            self.board[4][0].number = 6
            self.board[4][1].number = 0
            self.board[4][2].number = 0
            self.board[4][3].number = 0
            self.board[4][4].number = 3
            self.board[4][5].number = 8
            self.board[4][6].number = 7
            self.board[4][7].number = 1
            self.board[4][8].number = 0

            self.board[5][0].number = 4
            self.board[5][1].number = 0
            self.board[5][2].number = 2
            self.board[5][3].number = 7
            self.board[5][4].number = 0
            self.board[5][5].number = 0
            self.board[5][6].number = 0
            self.board[5][7].number = 0
            self.board[5][8].number = 0

            self.board[6][0].number = 0
            self.board[6][1].number = 0
            self.board[6][2].number = 0
            self.board[6][3].number = 2
            self.board[6][4].number = 0
            self.board[6][5].number = 3
            self.board[6][6].number = 0
            self.board[6][7].number = 7
            self.board[6][8].number = 6

            self.board[7][0].number = 3
            self.board[7][1].number = 0
            self.board[7][2].number = 0
            self.board[7][3].number = 0
            self.board[7][4].number = 0
            self.board[7][5].number = 0
            self.board[7][6].number = 1
            self.board[7][7].number = 6
            self.board[7][8].number = 7


            self.board[8][0].number = 0
            self.board[8][1].number = 0
            self.board[8][2].number = 5
            self.board[8][3].number = 0
            self.board[8][5].number = 0
            self.board[8][6].number = 0
            self.board[8][7].number = 0
            self.board[8][8].number = 8
            # ----------------------


    def number_is_in_row(self, number, row):
        for tile in self.board[row]:
            if tile.number == number:
                return True
        return False

    def check_violation_in_row(self, number, row, current_tile_column):
        _violations =0

        for column_index, tile in enumerate(self.board[row]):
            if column_index==current_tile_column:
               continue
            if tile.number==number:
                _violations+=1
        return _violations

    def number_is_in_column(self, number, column):
        for row in self.board:
            if row[column].number == number:
                return True
        return False

    def check_violation_in_column(self, number, column, current_tile_row):
        _violations =0
        for row_index, row in enumerate(self.board):
            if row_index==current_tile_row:
               continue
            if row[column].number==number:
                _violations +=1
        return _violations


    def number_available_in_restrictions(self, current_tile, number_to_add, row, column):
        if column > 0:
            previous_tile = self.board[row][column - 1]
            if previous_tile.restictions:
                for restriction in previous_tile.restictions:
                    if restriction == '<':
                        return number_to_add > previous_tile.number
                    elif restriction == '>':
                        return number_to_add < previous_tile.number
        if row > 0:
            upper_tile = self.board[row - 1][column]
            if upper_tile.restictions:
                for restriction in upper_tile.restictions:
                    if restriction == '^':
                        return number_to_add > upper_tile.number
                    elif restriction == 'V':
                        return number_to_add < upper_tile.number

        for restriction in current_tile.restictions:
            if restriction == '<':
                if self.board[row][column + 1].number > 0:
                    return number_to_add < self.board[row][column + 1].number
                return True
            elif restriction == '>':
                if self.board[row][column + 1].number > 0:
                    return number_to_add > self.board[row][column + 1].number and self.board[row][
                        column + 1].number < number_to_add
                return True
            elif restriction == '^':
                if self.board[row + 1][column].number > 0:
                    return number_to_add < self.board[row + 1][column].number
            else:
                if self.board[row + 1][column].number > 0:
                    return number_to_add > self.board[row + 1][column].number
        return True

    def print_matrix(self):
        str_board = self.board_to_str()
        print(str_board)

    def randomize_board(self):
        for row_index, row in enumerate(self.board):
            for column_index, column in enumerate(row):
                if not self.board[row_index][column_index].number:
                    self.board[row_index][column_index].number = random.randrange(1, self.dimension)
                    # self.board[row_index][column_index].number = 1

    def can_add_number(self, number, column, row):
        number_is_in_column = self.number_is_in_column(number, column)
        number_is_in_row = self.number_is_in_row(number, row)
        current_tile = self.board[row][column]
        number_available_in_restrictions = self.number_available_in_restrictions(current_tile, number, row, column)
        return not number_is_in_row and not number_is_in_column and number_available_in_restrictions

    def get_available_numbers_to_throw(self, row, column):
        if self.board[row][column].number > 0:
            return [self.board[row][column].number]
        available_numbers = []
        for number in range(1, self.dimension + 1):
            if self.can_add_number(number, column, row):
                available_numbers.append(number)
        return available_numbers

    def count_tile_restrictions_violations(self, current_tile, row, column):
        violations = 0
        violations += self.check_violation_in_column(current_tile.number,column,row)
        violations += self.check_violation_in_row(current_tile.number,row,column)

        # if column > 0:
        #     previous_tile = self.board[row][column - 1]
        #     if previous_tile.restictions:
        #         for restriction in previous_tile.restictions:
        #             if restriction == '<':
        #                 if number_to_add <= previous_tile.number:
        #                     violations += 1
        #             elif restriction == '>':
        #                 if number_to_add >= previous_tile.number:
        #                     violations += 1

        # if row > 0:
        #     upper_tile = self.board[row - 1][column]
        #     if upper_tile.restictions:
        #         for restriction in upper_tile.restictions:
        #             if restriction == '^':
        #                 if number_to_add <= upper_tile.number:
        #                     violations += 1
        #             elif restriction == 'V':
        #                 if number_to_add >= upper_tile.number:
        #                     violations += 1

        # for restriction in current_tile.restictions:
        #     if restriction == '<':
        #         if self.board[row][column + 1].number > 0:
        #             if number_to_add >= self.board[row][column + 1].number:
        #                 violations += 1
        #     elif restriction == '>':
        #         if self.board[row][column + 1].number > 0:
        #             if number_to_add <= self.board[row][column + 1].number and self.board[row][
        #                 column + 1].number >= number_to_add:
        #                 violations += 1
        #
        #     elif restriction == '^':
        #         if self.board[row + 1][column].number > 0:
        #             if number_to_add >= self.board[row + 1][column].number:
        #                 violations += 1
        #     else:
        #         if self.board[row + 1][column].number > 0:
        #             if number_to_add <= self.board[row + 1][column].number:
        #                 violations += 1
        return violations
    def board_to_str(self):
        str_board = ''
        for row in self.board:
            line = ' '.join([str(tile.number) + ''.join(tile.restictions) for tile in row])
            str_board += line + '\n'
        return str_board

    def refresh_violations(self):
        _violations = 0
        for row_index, row in enumerate(self.board):
            for column_index, column in enumerate(row):
                current_tile = self.board[row_index][column_index]
                _violations += self.count_tile_restrictions_violations(current_tile,row_index,column_index)
        self.violations = _violations

    def create_node(self, row, column, number):
        _env = copy.deepcopy(self)
        _env.board[row][column].number = number
        return Node(_env, row, column)
