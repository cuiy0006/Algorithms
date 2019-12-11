class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        
        res = []
        i = lower
        for num in nums:
            if num > upper:
                num = upper
            
            if i == num:
                i = num + 1
            elif i < num:
                if i == num - 1:
                    res.append(str(i))
                else:
                    res.append(str(i) + '->' + str(num - 1))
                i = num + 1
            
            if upper < i:
                break;
        
        if i == upper:
            res.append(str(i))
        elif i < upper:
            res.append(str(i) + '->' + str(upper))
        
        return res
