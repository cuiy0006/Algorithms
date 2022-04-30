class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        m = len(board)
        n = len(board[0])
        
        def live_neighbours(x, y):
            cnt = 0
            for x0, y0 in directions:
                x1, y1 = x+x0, y+y0
                if x1 < 0 or x1 > m-1 or y1 < 0 or y1 > n-1:
                    continue
                if board[x1][y1] == 1 or board[x1][y1] == 2:
                    cnt += 1
            return cnt
        
        for i in range(m):
            for j in range(n):
                live = live_neighbours(i, j)
                if board[i][j] == 0:
                    if live == 3:
                        board[i][j] = 3
                else:
                    if live != 2 and live != 3:
                        board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
