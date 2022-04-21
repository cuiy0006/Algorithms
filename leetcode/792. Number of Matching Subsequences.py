class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic = defaultdict(list) # start char -> rest str
        
        for word in words:
            dic[word[0]].append(word[1:])
        
        res = 0
        for c in s:
            if c not in dic:
                continue
            
            words = dic[c]
            del dic[c]
            for word in words:
                if word == '':
                    res += 1
                    continue
                dic[word[0]].append(word[1:])
        
        return res
