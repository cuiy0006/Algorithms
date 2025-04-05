class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = set(words)
        dic = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                pre = word[:i]+word[i+1:]
                if pre in words:
                    dic[pre].append(word)
        chain = {}
        def get_chain(word):
            if word in chain:
                return chain[word]
            cnt = 0
            for successor in dic[word]:
                cnt = max(cnt, get_chain(successor))
            chain[word] = cnt+1
            return chain[word]

        res = 0
        for word in words:
            res = max(res, get_chain(word))
        return res



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
        
