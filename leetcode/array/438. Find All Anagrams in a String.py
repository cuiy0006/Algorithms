class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic = defaultdict(int)
        for c in p:
            dic[c] += 1

        res = []
        cnt = len(dic)
        i = 0
        j = 0
        while j < len(s):
            if s[j] not in dic:
                while i < j:
                    dic[s[i]] += 1
                    if dic[s[i]] == 1:
                        cnt += 1
                    i += 1
                j += 1
                i = j
            elif dic[s[j]] == 0:
                while i < j and s[i] != s[j]:
                    dic[s[i]] += 1
                    if dic[s[i]] == 1:
                        cnt += 1
                    i += 1
                i += 1
                j += 1
                if cnt == 0:
                    res.append(i)
            else:
                dic[s[j]] -= 1
                if dic[s[j]] == 0:
                    cnt -= 1
                    if cnt == 0:
                        res.append(i)
                j += 1
        return res
