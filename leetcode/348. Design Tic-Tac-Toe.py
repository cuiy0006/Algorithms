class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row = [0 for i in range(n)]
        self.col = [0 for i in range(n)]
        self.diag = 0
        self.rev_diag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        val = 1 if player == 1 else -1
        self.row[row] += val
        if abs(self.row[row]) == self.n:
            return player
        self.col[col] += val
        if abs(self.col[col]) == self.n:
            return player
        if row == col:
            self.diag += val
            if abs(self.diag) == self.n:
                return player
        if row + col == self.n - 1:
            self.rev_diag += val
            if abs(self.rev_diag) == self.n:
                return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
