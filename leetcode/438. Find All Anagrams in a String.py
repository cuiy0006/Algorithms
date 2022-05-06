class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic = defaultdict(int)
        
        for c in p:
            dic[c] += 1
        
        cnt = len(dic)
        res = []
        
        for i, c in enumerate(s):
            if i < len(p):
                if c in dic:
                    dic[c] -= 1
                    if dic[c] == 0:
                        cnt -= 1
                        if cnt == 0:
                            res.append(0)
            else:
                c0 = s[i-len(p)]
                if c0 in dic:
                    dic[c0] += 1
                    if dic[c0] == 1:
                        cnt += 1
                if c in dic:
                    dic[c] -= 1
                    if dic[c] == 0:
                        cnt -= 1
                        if cnt == 0:
                            res.append(i-len(p)+1)
        
        return res




class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic = {}
        for c in p:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        n = len(p)
        res = []
        
        for i, c in enumerate(s):
            j = i - len(p)
            if i >= len(p):
                if s[j] in dic:
                    dic[s[j]] += 1
                    if dic[s[j]] > 0:
                        n += 1
            
            if c in dic:
                dic[c] -= 1
                if dic[c] >= 0:
                    n -= 1

            if n == 0:
                res.append(i - len(p) + 1)
                
        return res
            
