class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0, 0, 0, 0, 0] for i in range(n)]
        dp[0] = [1, 1, 1, 1, 1]
        MOD = 10 ** 9 + 7
        for i in range(1, n):
            dp[i][0] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]
            dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
            dp[i][2] = dp[i - 1][1] + dp[i - 1][3]
            dp[i][3] = dp[i - 1][2]
            dp[i][4] = dp[i - 1][2] + dp[i - 1][3]
            
        return sum(dp[-1]) % MOD
