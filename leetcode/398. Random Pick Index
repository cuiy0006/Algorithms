from random import randint
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        self.size = 2 ** 31

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt = 0
        res = -1
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                if randint(1, self.size) % cnt == 0:
                    res = i
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
