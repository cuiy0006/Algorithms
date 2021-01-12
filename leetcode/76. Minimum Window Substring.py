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


    
    
from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = {}
        for c in t:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        
        cnt = len(dic)
        indexes = deque()
        start = None
        end = None
        
        for i, c in enumerate(s):
            if c not in dic:
                continue
            dic[c] -= 1
            indexes.append(i)
            if cnt > 0 and dic[c] == 0:
                cnt -= 1
                if cnt == 0:
                    start = indexes[0]
                    end = indexes[-1]
            while len(indexes) != 0 and dic[s[indexes[0]]] < 0:
                dic[s[indexes[0]]] += 1
                indexes.popleft()
            if cnt == 0 and indexes[-1] - indexes[0] < end - start:
                start = indexes[0]
                end = indexes[-1]
                
        if start == None:
            return ''
        else:
            return s[start: end + 1]
