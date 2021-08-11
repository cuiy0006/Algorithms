class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic = {}
        for word in words:
            if word[0] not in dic:
                dic[word[0]] = []
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
                else:
                    if word[0] not in dic:
                        dic[word[0]] = []
                    dic[word[0]].append(word[1:])
            
            
        return res
