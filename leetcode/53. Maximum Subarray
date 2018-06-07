class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = -sys.maxsize
        curr = 0
        for i, num in enumerate(nums):
            curr += num
            maxVal = max(maxVal, curr)
            if curr < 0:
                curr = 0
        return maxVal
