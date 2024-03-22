class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [False for _ in range(n)]
        diag = [False for _ in range(2*n-1)]
        rev_diag = [False for _ in range(2*n-1)]

        res = 0
        def helper(row, curr):
            if row == n:
                nonlocal res
                res += 1
                return
            
            for col in range(n):
                if not cols[col] and not diag[row-col+n-1] and not rev_diag[row+col]:
                    cols[col] = True
                    diag[row-col+n-1] = True
                    rev_diag[row+col] = True
                    curr[row][col] = 'Q'
                    helper(row+1, curr)
                    cols[col] = False
                    diag[row-col+n-1] = False
                    rev_diag[row+col] = False
                    curr[row][col] = '.'
        
        curr = [['.' for _ in range(n)] for _ in range(n)]
        helper(0, curr)
        return res