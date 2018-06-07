class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        i = m
        j = n
        for op in ops:
            i = min(i, op[0])
            j = min(j, op[1])
            
        return i * j
