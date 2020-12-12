class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                    
        return dp[-1][-1]
        
        

from collections import deque
D = [(0,1), (1,0)]
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        q = deque([(0, 0)])
        while len(q) != 0:
            x, y = q.popleft()
            for x0, y0 in D:
                x1, y1 = x + x0, y + y0
                if x1 >= m or y1 >= n:
                    continue
                visited = dp[x1][y1] != 0
                dp[x1][y1] += dp[x][y]
                if not visited:
                    q.append((x1, y1))
        return dp[-1][-1]
