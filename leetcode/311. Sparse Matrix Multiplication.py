class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(A[0])
        p = len(B[0])
        res = [[0 for i in range(p)] for j in range(m)]
        for i in range(m):
            for k in range(n):
                if A[i][k] == 0:
                    continue
                for j in range(p):
                    if B[k][j] == 0:
                        continue
                    res[i][j] += A[i][k]*B[k][j]
        return res
