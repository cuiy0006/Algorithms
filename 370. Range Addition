class Solution:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for lst in updates:
            start, end, inc = lst
            res[start] += inc
            if end + 1 < length:
                res[end+1] -= inc
        
        curr = 0
        for i, _ in enumerate(res):
            curr += res[i]
            res[i] = curr
        return res
