class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = defaultdict(int)
        for c in t:
            dic[c] += 1
        
        cnt = len(dic)
        i = 0
        j = 0
        res = ''

        while j < len(s):
            if s[j] not in dic:
                j += 1
            else:
                dic[s[j]] -= 1
                if dic[s[j]] == 0:
                    cnt -= 1
                j += 1
            
            while i < j:
                if s[i] not in dic:
                    i += 1
                else:
                    if dic[s[i]] < 0:
                        dic[s[i]] += 1
                        i += 1
                    else:
                        break
            if cnt == 0:
                if res == '' or len(res) > j - i:
                    res = s[i:j]
        return res
