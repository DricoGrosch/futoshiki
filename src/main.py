import random


class Environment:
    dimension = None
    board = []
    difficulty = 1

    def number_is_in_row(self, number, row):
        return number in self.board[row]

    def number_is_in_column(self, number, column):
        for row in self.board:
            if row[column] == number:
                return True
        return False

    def print_matrix(self):
        str_board = ''
        for row in self.board:
            line = ' '.join([str(value) for value in row])
            str_board += line + '\n'
        print(str_board)

    def can_add_number(self, number, column, row):
        number_is_in_column = self.number_is_in_column(number, column)
        number_is_in_row = self.number_is_in_row(number, row)
        return not number_is_in_row and not number_is_in_column

    def __init__(self, dimension=4):
        self.dimension = dimension
        for i in range(dimension):
            self.board.append([0 for j in range(dimension)])
        for i in range(5):
            number = int(random.randrange(1, dimension))
            column = int(random.randrange(0, dimension - 1))
            row = int(random.randrange(0, dimension - 1))
            if self.can_add_number(number, column, row) and self.board[row][column] == 0:
                self.board[row][column] = number


env = Environment()
env.print_matrix()
