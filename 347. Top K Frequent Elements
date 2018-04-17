class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        
        lst = [(num, freq) for num, freq in dic.items()]
        lst.sort(key = lambda x:-x[1])
        lst = lst[:k]
        return [num for num, _ in lst]
        
        
  
  
from heapq import heappush
from heapq import heappop

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        
        lst = []
        for num, freq in dic.items():
            heappush(lst, (freq, num))
            if len(lst) > k:
                heappop(lst)
        
        res = []
        while len(lst) != 0:
            res.append(heappop(lst)[1])
        res.reverse()
        return res
