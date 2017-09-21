class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {target-num:i for i, num in enumerate(nums)}
        for i,num in enumerate(nums):
            if num in dic and i != dic[num]:
                return [i, dic[num]]
