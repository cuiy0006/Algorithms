class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [-sys.maxsize] * 3
        for num in nums:
            if num > res[0]:
                res[0], res[1], res[2] = num, res[0], res[1]
            elif num > res[1] and num < res[0]:
                res[1], res[2] = num, res[1]
            elif num > res[2] and num < res[1]:
                res[2] = num
        if res[2] == -sys.maxsize:
            return res[0]
        else:
            return res[2]
