class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        i = 2
        while i < len(nums):
            if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                break
            i += 1
        j = i + 1
        while j < len(nums):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1
        return i
