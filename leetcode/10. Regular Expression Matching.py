class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False for i in range(n+1)] for j in range(m+1)]
        dp[0][0] = True
        for j in range(n):
            if p[j] == '*' and dp[0][j-1]:
                dp[0][j+1] = True
        for i in range(m):
            for j in range(n):
                if s[i] == p[j] or p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                else:
                    if p[j] == '*':
                        if s[i] == p[j-1] or p[j-1] == '.':
                            dp[i+1][j+1] = dp[i+1][j-1] or dp[i+1][j] or dp[i][j+1]
                        else:
                            dp[i+1][j+1] = dp[i+1][j-1]
        return dp[-1][-1]
