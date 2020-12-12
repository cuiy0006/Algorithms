class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        tmp = nums[0]
        for i in range(1, len(nums)):
            tmp ^= nums[i]
        
        for num in range(len(nums)+1):
            tmp ^= num
        return tmp
