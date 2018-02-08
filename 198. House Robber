class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        for i, profit in enumerate(nums):
            firstOption = 0
            secondOption = 0
            if i >= 2:
                firstOption = nums[i-2]
            if i >= 3:
                secondOption = nums[i-3]
            nums[i] = profit + max(firstOption, secondOption)
        return max(nums)
