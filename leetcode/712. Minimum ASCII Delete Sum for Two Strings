class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + ord(s1[i])
                else:
                    dp[i+1][j +1] = max(dp[i][j + 1], dp[i +1][j])
        total = 0
        for c in s1:
            total += ord(c)
        for c in s2:
            total += ord(c)
        return total - dp[-1][-1]*2
