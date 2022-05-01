class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_to_len = {'': 0}
        words.sort(key=lambda word:len(word))
        
        res = 0
        for word in words:
            max_len = 1
            for i in range(len(word)):
                last = word[:i] + word[i+1:]
                if last in word_to_len:
                    max_len = max(max_len, word_to_len[last]+1)
            word_to_len[word] = max_len
            res = max(res, max_len)
        
        return res
        
