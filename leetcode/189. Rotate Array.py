class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        
        def helper(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        helper(0, len(nums) - k - 1)
        helper(len(nums) - k, len(nums) - 1)
        helper(0, len(nums) - 1)
