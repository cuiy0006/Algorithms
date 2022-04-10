class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[0] = points[0][:]
        
        for i in range(1, m):
            # dp[i][j] = max(dp[i][j], points[i][j] + dp[i-1][k] - abs(j-k))
            # k < j: points[i][j] + dp[i-1][k] + k - j
            # k > j: points[i][j] + dp[i-1][k] - k + j
            
            left_dp = [0 for _ in range(n)]
            right_dp = [0 for _ in range(n)]
            left_dp[0] = dp[i-1][0]
            right_dp[n-1] = dp[i-1][n-1] - n + 1
            
            for k in range(1, n):
                left_dp[k] = max(left_dp[k-1], dp[i-1][k] + k)
            for k in range(n-2, -1, -1):
                right_dp[k] = max(right_dp[k+1], dp[i-1][k] - k)

            for j in range(n):
                dp[i][j] = points[i][j] + max(left_dp[j] - j, right_dp[j] + j)
        
        return max(dp[-1])
