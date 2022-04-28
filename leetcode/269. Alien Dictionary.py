from collections import deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        in_dic = defaultdict(int)
        dic = defaultdict(set)
        
        for word in words:
            for c in word:
                in_dic[c] = 0
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            if len(word1) > len(word2) and word1.startswith(word2):
                return ''
            
            for i in range(min(len(word1), len(word2))):
                if word1[i] == word2[i]:
                    continue
                    
                if word1[i] not in dic[word2[i]]:
                    dic[word2[i]].add(word1[i])
                    in_dic[word1[i]] += 1
                break
            
        q = deque()
        for c, degree in in_dic.items():
            if degree == 0:
                q.append(c)
        
        res = []
        while len(q) != 0:
            c = q.popleft()
            res.append(c)
            for c0 in dic[c]:
                in_dic[c0] -= 1
                if in_dic[c0] == 0:
                    q.append(c0)
        
        if len(res) != len(in_dic):
            return ''
        
        res.reverse()
        return ''.join(res)
        
        
