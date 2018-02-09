class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                cnt += (num >> i) & 1
            res |= (cnt % 3) << i
        if res >= 2 ** 31:
            res -= 2 ** 32
        return res
