class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.row = [0 for i in range(n)]
        self.col = [0 for i in range(n)]
        self.diag = 0
        self.rev_diag = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            add = 1
        else:
            add = -1
        self.row[row] += add
        if self.row[row] == self.n or self.row[row] == -self.n:
            return player
        self.col[col] += add
        if self.col[col] == self.n or self.col[col] == -self.n:
            return player
        if row == col:
            self.diag += add
            if self.diag == self.n or self.diag == -self.n:
                return player
        if row + col == self.n - 1:
            self.rev_diag += add
            if self.rev_diag == self.n or self.rev_diag == -self.n:
                return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
