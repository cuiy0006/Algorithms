class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        maxlen = 1
        curr = nums[0]
        j = 0
        i = 1
        while i < len(nums):
            if nums[i] <= curr:
                maxlen = max(maxlen, i - j)
                j = i
            curr = nums[i]
            i += 1
        return max(maxlen, i - j)
