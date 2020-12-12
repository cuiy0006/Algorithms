class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        dic = {}
        res = 0
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        for num, cnt in dic.items():
            if k == 0:
                if cnt > 1:
                    res += 1
            else:
                if num + k in dic:
                    res += 1
        return res
