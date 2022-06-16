import random

class Environment:
    def finish(self):
        has_empty_value=False
        for row in self.board:
            if 0 in row:
                has_empty_value=True
        return not has_empty_value

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

    def __init__(self, dimension=4,random_start=True):
        self.dimension = dimension
        self.board=[]
        for i in range(dimension):
            self.board.append([0 for j in range(dimension)])

        if random_start:
            for i in range(5):
                number = int(random.randrange(1, dimension))
                column = int(random.randrange(0, dimension - 1))
                row = int(random.randrange(0, dimension - 1))
                if self.can_add_number(number, column, row) and self.board[row][column] == 0:
                    self.board[row][column] = number
        else:
            # self.board[0][0] = 2
            # self.board[0][1] = 3
            # self.board[0][3] = 1
            # self.board[1][0] = 1
            # self.board[1][3] = 2
            # self.board[2][1] = 1
            # self.board[2][3] = 3
            self.board[0][0] = 2
            self.board[1][1] = 1
            self.board[1][3] = 3
            self.board[3][2] = 1
            self.board[3][3] = 2

    def copy(self,row_index_to_change,column_index_to_change,number):
        new_environment = Environment()
        new_environment.dimension = 4
        new_environment.board = [*self.board]
        new_environment.board[row_index_to_change][column_index_to_change]=number
        new_environment.difficulty = 3
        return new_environment
