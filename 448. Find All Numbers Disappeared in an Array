class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i, num in enumerate(nums):
            if num > 0:
                index = num - 1
                while index >= 0:
                    nums[index], index = -1, nums[index] - 1
                    
        
        res = [i + 1 for i, num in enumerate(nums) if num != -1]
        return res
