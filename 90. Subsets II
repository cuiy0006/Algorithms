#recursive
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def helper(index, lst):
            if index <= len(nums):
                res.append(lst[:])
            if index == len(nums):
                return
            
            i = index
            while i < len(nums):
                lst.append(nums[i])
                helper(i+1, lst)
                lst.pop()
                i += 1
                while i < len(nums) and nums[i] == nums[i-1]:
                    i += 1
        helper(0, [])
        return res
        
        
#iterative
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        size = 0
        for i, num in enumerate(nums):
            start = 0
            if i != 0 and nums[i] == nums[i-1]:
                start = size
            size = len(res)
            for j in range(start, size):
                lst = res[j][:]
                lst.append(nums[i])
                res.append(lst)
        return res
        
        
