class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        avg = 0
        for i in range(k):
            avg += nums[i]
        curr = avg
        for i in range(k, len(nums)):
            curr = curr - nums[i-k] + nums[i]
            avg = max(avg, curr)
        return avg / k
