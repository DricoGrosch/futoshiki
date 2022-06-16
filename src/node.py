
class Node:
    env=None
    row=None
    column=None

    def get_value(self):
        return self.env.board[self.row][self.column]

    def __init__(self,env,row,column):
        self.env=env
        self.row=row
        self.column=column