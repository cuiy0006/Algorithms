class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i):
                word = s[j:i]
                if word in wordDict and dp[j]:
                    dp[i] = True
        return dp[-1]
