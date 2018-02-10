class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = nums[0]
        minVal = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            maxVal, minVal = max(num, num * minVal, num * maxVal), min(num, num * minVal, num * maxVal)
            res = max(res, maxVal)
        return res
