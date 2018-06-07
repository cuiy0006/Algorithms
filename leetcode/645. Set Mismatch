class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        dup = None
        nonDup = None
        large = max(nums)
        for num in nums:
            if num in s:
                dup = num
            else:
                s.add(num)
        
        for i in range(1, large+1):
            if i not in s:
                nonDup = i
                break
        
        if nonDup == None:
            nonDup = large + 1
        return (dup, nonDup)
