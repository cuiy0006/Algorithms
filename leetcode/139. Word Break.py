class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = max([len(word) for word in wordDict])
        word_set = set(wordDict)
        
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(len(s)):
            if not dp[i]:
                continue
            for j in range(i, min(len(s), i+max_len)):
                word = s[i:j+1]
                if word in word_set:
                    dp[j+1] = True

        return dp[-1]
