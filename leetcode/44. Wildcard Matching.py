class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """        
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        for j, c in enumerate(p):
            if c != '*':
                break
            dp[0][j+1] = True

        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    if p[j] == '?':
                        dp[i+1][j+1] = dp[i][j]
                    elif p[j] == '*':
                        dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]
        return dp[-1][-1]
