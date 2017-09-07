class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(len(M[0]))] for j in range(len(M))]
        d = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1],[0,0]]
        for i in range(len(M)):
            for j in range(len(M[0])):
                cnt = 0
                total = 0
                for adder in d:
                    x = i + adder[0]
                    y = j + adder[1]
                    if x >= 0 and x < len(M) and y >= 0 and y < len(M[0]):
                        cnt += 1
                        total += M[x][y]
                res[i][j] = total // cnt
        return res
