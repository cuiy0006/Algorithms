class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        i = 1
        j = 1
        while j < len(nums):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
