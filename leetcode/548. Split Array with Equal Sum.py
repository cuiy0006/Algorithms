class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        target = 0
        total = sum(nums)
        for i in range(1, n-5):
            if i != 1 and nums[i-1]==0 and nums[i] == 0:
                continue
            target += nums[i - 1]
            j_start = i + 1
            left = total - nums[i] - target
            if self.j_helper(nums, target, j_start, left):
                return True
        return False
    
    def j_helper(self, nums, target, start, left):
        j_target = 0
        n = len(nums)
        for j in range(start+1, n-3):
            j_target += nums[j-1]
            k_left = left - nums[j] - j_target
            k_start = j + 1
            if j_target == target and self.k_helper(nums, target, k_start, k_left):
                return True
        return False
    
    def k_helper(self, nums, target, start, left):
        k_target = 0
        n = len(nums)
        for k in range(start + 1, n-1):
            k_target += nums[k-1]
            last_left = left - nums[k] - k_target
            if k_target == target and last_left == target:
                return True
        return False
