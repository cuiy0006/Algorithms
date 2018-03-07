from random import randint
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[randint(0, len(nums)-1)]
        cnt = 0
        left = []
        right = []
        for num in nums:
            if num == pivot:
                cnt += 1
            elif num > pivot:
                left.append(num)
            else:
                right.append(num)
        if k <= len(left):
            return self.findKthLargest(left, k)
        elif k > len(left) and k <= len(left) + cnt:
            return pivot
        else:
            return self.findKthLargest(right, k - len(left) - cnt)
