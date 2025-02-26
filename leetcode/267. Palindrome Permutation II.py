class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        dic = {}
        single = ''
        for c in s:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        
        for c, cnt in dic.items():
            if cnt % 2 != 0:
                if single != '':
                    return []
                single = c
        if single in dic:
            dic[single] -= 1
            if dic[single] == 0:
                del dic[single]
        
        res = []
        def helper(curr):
            if len(dic) == 0:
                res.append(curr)
                return
            keys = list(dic.keys())
            for c in keys:
                dic[c] -= 2
                if dic[c] == 0:
                    del dic[c]
                helper(c + curr + c)
                if c not in dic:
                    dic[c] = 0
                dic[c] += 2
        helper(single)
        return res
