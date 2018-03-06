class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            sub = []
            for lst in res:
                tmp = lst[:]
                tmp.append(num)
                sub.append(tmp)
            res += sub
        return res
