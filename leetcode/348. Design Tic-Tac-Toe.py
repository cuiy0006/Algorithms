class TicTacToe:

    def __init__(self, n: int):
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.rev_diag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        delta = 1 if player == 1 else -1
        self.row[row] += delta
        self.col[col] += delta
        if row == col:
            self.diag += delta
        if row + col == self.n-1:
            self.rev_diag += delta
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diag) == self.n or abs(self.rev_diag) == self.n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
