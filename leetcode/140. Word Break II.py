class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dic = {}
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        wordDict = set(wordDict)
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] == 1 and s[j:i] in wordDict:
                    dp[i] = 1
                    if i in dic:
                        dic[i].append(s[j:i])
                    else:
                        dic[i] = [s[j:i]]
                        
        res = []
        if dp[-1] == 0:
            return res
        
        def helper(idx, tmp):
            if idx == 0:
                res.append(tmp)
                return
            
            for word in dic[idx]:
                l = len(word)
                if tmp != '':
                    word += ' ' + tmp
                helper(idx - l, word)
        
        helper(len(s), '')
        return res
