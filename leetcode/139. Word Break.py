class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(wordDict) == 0:
            return False
        dic = set(wordDict)
        dp = [False] * len(s)
        maxlen = len(max(wordDict, key=lambda x:len(x)))
        for i in range(len(s)):
            j = i
            while j >= 0 and i - j < maxlen:
                sub = s[j:i+1]
                if sub in dic and (j == 0 or dp[j-1]):
                    dp[i] = True
                    break
                j -= 1
        return dp[-1]
