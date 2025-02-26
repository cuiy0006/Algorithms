class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(start, curr):
            res.append(curr[:])
            for i in range(start, len(nums)):
                curr.append(nums[i])
                helper(i+1, curr)
                curr.pop()
        helper(0, [])
        return res


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
