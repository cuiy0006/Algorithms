class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        minlen = sys.maxsize
        i = 0
        j = 0
        curr = 0
        while j < len(nums):
            curr += nums[j]
            while curr >= s and i <= j:
                minlen = min(minlen, j - i + 1)
                curr -= nums[i]
                i += 1
            j += 1
        if minlen == sys.maxsize:
            return 0
        return minlen
