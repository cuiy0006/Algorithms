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
    
    
    
    
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(len(dp)):
            reached = dp[i]
            if not reached:
                continue

            for word in words:
                if i + len(word) > len(s):
                    continue
                if s[i: i + len(word)] == word:
                    dp[i + len(word)] = True

        return dp[-1]
