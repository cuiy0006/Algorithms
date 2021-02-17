class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [True for _ in range(n)]
        ldiag = [True for _ in range(2 * n - 1)]
        rdiag = [True for _ in range(2 * n - 1)]
        res = []
        curr = [['.' for _ in range(n)] for _ in range(n)]
        
        def helper(x, y):
            if not cols[y] or not ldiag[n-1+x-y] or not rdiag[x+y]:
                return
            
            cols[y] = ldiag[n-1+x-y] = rdiag[x+y] = False
            curr[x][y] = 'Q'
            
            if x == n - 1:
                tmp = [''.join(lst) for lst in curr]
                res.append(tmp)
                cols[y] = ldiag[n-1+x-y] = rdiag[x+y] = True
                curr[x][y] = '.'
                return
            
            for i in range(n):
                helper(x + 1, i)
                
            cols[y] = ldiag[n-1+x-y] = rdiag[x+y] = True
            curr[x][y] = '.'
            
        for i in range(n):
            helper(0, i)
            
        return res
