class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        idx = 0
        lst = [0]
        while idx < n:
            sub = []
            for i, num in enumerate(lst):
                sub.append((1<<idx)|num)
            lst = lst + list(reversed(sub))
            idx += 1
        return lst
