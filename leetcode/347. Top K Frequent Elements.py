class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        max_freq = 0
        for num in nums:
            dic[num] += 1
            max_freq = max(max_freq, dic[num])
        
        lst = [(freq, num) for num, freq in dic.items()]
        buckets = [[] for _ in range(max_freq+1)]

        for num, freq in dic.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets)-1, -1, -1):
            lst = buckets[i]
            res += lst[:min(k-len(res), len(lst))]
            if len(res) == k:
                break
        return res
        
        
  
  
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
