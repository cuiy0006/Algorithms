class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return board
        def helper(x, y):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return
            if board[x][y] == 'X' or board[x][y] == '#':
                return
            board[x][y] = '#'
            helper(x + 1, y)
            helper(x - 1, y)
            helper(x, y + 1)
            helper(x, y - 1)
            
            
        for i in range(len(board)):
            if board[i][0] == 'O':
                helper(i, 0)
            if board[i][len(board[0]) - 1] == 'O':
                helper(i, len(board[0]) - 1)
        
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                helper(0, j)
            if board[len(board) - 1][j] == 'O':
                helper(len(board) - 1, j)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
