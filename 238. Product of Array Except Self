class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        curr = 1
        for i in range(len(nums)-1, -1, -1):
            if i != len(nums) - 1:
                res[i] = res[i] * curr
            curr = curr * nums[i]
        return res
