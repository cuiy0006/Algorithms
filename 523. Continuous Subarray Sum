class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {0: -1}
        total = 0
        for i in range(len(nums)):
            if k != 0:
                total = (total + nums[i]) % k
            else:
                total = total + nums[i]
            if total in dic:
                if i - dic[total] >= 2:
                    return True
            else:
                dic[total] = i
        return False
