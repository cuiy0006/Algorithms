class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        rows = [-1] * n # rows[i] is col for row i
        res = [0]

        def helper(row):
            if row == n:
                res[0] += 1
                return

            for j in range(n):
                is_available = True
                for i in range(row):
                    used_col = rows[i]
                    if used_col == j or abs(used_col - j) == abs(i - row):
                        is_available = False
                        break

                if is_available:
                    rows[row] = j
                    helper(row + 1)
        helper(0)
        return res[0]