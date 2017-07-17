class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxArr = [-sys.maxsize, -sys.maxsize, -sys.maxsize]
        minArr = [sys.maxsize, sys.maxsize]
        
        for num in nums:
            if num > maxArr[2]:
                maxArr[2], maxArr[1], maxArr[0] = num, maxArr[2], maxArr[1]
            elif num > maxArr[1]:
                maxArr[1], maxArr[0] = num, maxArr[1]
            elif num > maxArr[0]:
                maxArr[0] = num
                
            if num < minArr[1]:
                minArr[1], minArr[0] = num, minArr[1]
            elif num < minArr[0]:
                minArr[0] = num
                
        return max(minArr[0] * minArr[1] * maxArr[2], maxArr[0] * maxArr[1] * maxArr[2])
