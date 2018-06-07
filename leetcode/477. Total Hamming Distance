class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in range(32):
            zeros = 0
            ones = 0
            for i, num in enumerate(nums):
                if num & 1 == 1:
                    ones += 1
                else:
                    zeros += 1
                nums[i] = nums[i] >> 1
            total += ones * zeros
        return total
