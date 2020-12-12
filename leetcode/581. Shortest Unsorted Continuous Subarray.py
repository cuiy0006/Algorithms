class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = sorted(nums)
        left = -1
        right = -1
        for i in range(len(nums)):
            if nums[i] != lst[i]:
                left = i
                break
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != lst[i]:
                right = i
                break
        
        if left == -1:
            return 0
        return right - left + 1
