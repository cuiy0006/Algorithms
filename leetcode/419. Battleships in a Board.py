class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        
        def helper(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if board[x][y] == '.':
                return
            board[x][y] = '.'
            for x0, y0 in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                helper(x+x0, y+y0)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    helper(i, j)
                    res += 1
        
        return res
