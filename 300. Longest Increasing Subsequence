class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        lst = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > lst[-1]:
                lst.append(nums[i])
                continue
            left = 0
            right = len(lst)
            while left < right:
                mid = (left + right) // 2
                if lst[mid] >= nums[i]:
                    right = mid
                else:
                    left = mid + 1
            lst[left] = nums[i]
        return len(lst)
