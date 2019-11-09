class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [0 for i in range(len(s)+1)]
        dic = set([str(i) for i in range(1, 27)])
        dp[0] = 1
        for i in range(0, len(s)):
            if s[i] == '0':
                if i == 0 or s[i-1:i+1] not in dic:
                    return 0
                dp[i+1] = dp[i-1]
                continue
            dp[i+1] = dp[i]
            if i == 0:
                continue
            num = s[i-1:i+1]
            if num in dic:
                dp[i+1] += dp[i-1]
        return dp[-1]
