class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = [-1 for i in range(26)]
        for i, c in enumerate(S):
            dic[ord(c) - ord('a')] = i
        
        m = n = 0
        res = []
        for i in range(len(S)):
            c = S[i]
            n = max(dic[ord(c) - ord('a')], n)
            if i >= n:
                res.append(n - m + 1)
                m = n = i + 1
        return res
            
