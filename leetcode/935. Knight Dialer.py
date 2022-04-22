



class Solution:
    def knightDialer(self, n: int) -> int:
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
        
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        
        @cache
        def find_path(i, j, step):
            if i < 0 or i > 3 or j < 0 or j > 2 or (i == 3 and j == 0) or (i == 3 and j == 2):
                return 0
            
            if step == 1:
                cnt = 1
            else:
                cnt = 0
                for x0, y0 in directions:
                    cnt += find_path(i+x0, j+y0, step-1)
            
            return cnt % 1000000007

        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                res += find_path(i, j, n)
        
        return res % 1000000007
