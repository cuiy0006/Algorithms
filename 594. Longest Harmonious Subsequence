class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        res = 0    
        for num, cnt in dic.items():
            if num + 1 in dic:
                res = max(res, cnt + dic[num + 1])
            if num - 1 in dic:
                res = max(res, cnt + dic[num - 1])
            
        return res
