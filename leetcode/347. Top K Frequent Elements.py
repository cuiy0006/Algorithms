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
        
        
  
  
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
            
        freqs = []
        for num, freq in dic.items():
            if len(freqs) == k:
                if freqs[0][0] < freq:
                    heappop(freqs)
                    heappush(freqs, (freq, num))
            else:
                heappush(freqs, (freq, num))
        return [num for _, num in freqs]
