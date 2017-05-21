class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        curr = 0
        cnt = 0
        for num in nums:
            curr += num
                
            if curr == k:
                cnt += 1
                
            if curr - k in dic:
               cnt += dic[curr - k]
               
            if curr in dic:
                dic[curr] += 1
            else:
                dic[curr] = 1
        return cnt
