class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i, j, start, end = 0, 0, 0, 0
        minlen = sys.maxsize
        cnt = len(t)
        dic = {}
        for c in t:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        while j < len(s):
            if s[j] not in dic:
                j += 1
                continue
            if dic[s[j]] > 0:
                cnt -= 1
            dic[s[j]] -= 1
            j += 1
            while cnt == 0:
                if s[i] not in dic:
                    i += 1
                    continue
                if j - i < minlen:
                    minlen = j - i
                    start = i
                    end = j
                if dic[s[i]] == 0:
                    cnt += 1
                dic[s[i]] += 1
                i += 1
        return s[start:end]


    
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = {}
        for c in t:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        
        i = 0
        j = 0
        cnt = 0
        res_i = None
        res_j = None
        
        while j < len(s):
            c = s[j]
            if c in dic:
                dic[c] -= 1
                if dic[c] == 0:
                    cnt += 1
                if cnt == len(dic):
                    if res_i is None and res_j is None:
                        res_i = i
                        res_j = j
                    
                    while i <= j:
                        if j - i < res_j - res_i:
                            res_i = i
                            res_j = j
                        
                        c = s[i]
                        if c in dic:
                            dic[c] += 1
                            if dic[c] > 0:
                                cnt -= 1
                                i += 1
                                break
                        i += 1
            j += 1
        
        if res_i is None or res_j is None:
            return ""
        return s[res_i:res_j+1]
