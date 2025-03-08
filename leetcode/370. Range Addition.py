class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        dic = defaultdict(int)
        for [start, end, inc] in updates:
            dic[start] += inc
            dic[end+1] -= inc
        
        res = [None] * length
        curr = 0
        for i in range(length):
            if i in dic:
                curr += dic[i]
            res[i] = curr
        return res
