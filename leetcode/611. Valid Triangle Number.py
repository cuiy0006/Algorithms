class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        if len(nums) < 3:
            return cnt
        nums.sort()
        for i, num in enumerate(nums):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > num:
                    cnt += right - left
                    right -= 1
                else:
                    left += 1
        return cnt
