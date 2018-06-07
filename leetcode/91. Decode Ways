class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0 for i in range(len(s))]
        dp[0] = 1
        if s[1] != '0':
            dp[1] = dp[0]
        if (s[0] == '1') or (s[0] =='2' and s[1]>='0' and s[1] <='6'):
            dp[1] += 1
        for i in range(2, len(s)):
            if s[i] != '0':
                dp[i] = dp[i-1]
            if (s[i-1] == '1') or (s[i-1] =='2' and s[i]>='0' and s[i] <='6'):
                dp[i] += dp[i-2]
        return dp[-1]
