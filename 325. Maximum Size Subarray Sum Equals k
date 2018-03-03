class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        dic = {0:-1}
        maxlen = 0
        for i, num in enumerate(nums):
            total += num
            if total not in dic:
                dic[total] = i
            if (total - k) in dic:
                maxlen = max(maxlen, i - dic[total-k])
        return maxlen
