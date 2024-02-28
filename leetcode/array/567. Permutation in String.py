class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = defaultdict(int)
        for c in s1:
            dic[c] += 1
        
        cnt = len(dic)
        i = 0
        j = 0
        while j < len(s2):
            if s2[j] not in dic:
                while i < j:
                    dic[s2[i]] += 1
                    if dic[s2[i]] == 1:
                        cnt += 1
                    i += 1
                j += 1
                i = j
            elif dic[s2[j]] == 0:
                while i < j and s2[i] != s2[j]:
                    dic[s2[i]] += 1
                    if dic[s2[i]] == 1:
                        cnt += 1
                    i += 1
                i += 1
                j += 1
            else:
                dic[s2[j]] -= 1
                if dic[s2[j]] == 0:
                    cnt -= 1
                    if cnt == 0:
                        return True
                j += 1
        return False
