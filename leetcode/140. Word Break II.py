class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        
        word_set = set(wordDict)
        
        maxlen = max([len(word) for word in word_set])
        
        idx_to_words = defaultdict(list)
        
        i = 0
        while i < len(s):
            if not dp[i]:
                i += 1
                continue
            j = i
            while j < min(len(s), i+maxlen):
                word = s[i:j+1]
                if word in word_set:
                    dp[j+1] = True
                    idx_to_words[j+1].append(word)
                j += 1
            i += 1

        res = []
        
        def get_words(idx, curr):
            if idx == 0:
                res.append(curr)
                return

            for word in idx_to_words[idx]:
                new_s = word if curr == '' else word + ' ' + curr
                get_words(idx-len(word), new_s)
                
        get_words(len(s), '')
        return res
        
