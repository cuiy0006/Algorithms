from heapq import heappush
from heapq import heappop
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic = {}
        for task in tasks:
            if task in dic:
                dic[task] += 1
            else:
                dic[task] = 1
        h = []
        cnt = 0
        for v in dic.values():
            heappush(h, -v)
        while len(h) != 0:
            k = n + 1
            lst = []
            while k > 0 and len(h) != 0:
                freq = heappop(h)
                if freq + 1 < 0:
                    lst.append(freq+1)
                cnt += 1
                k -= 1
            for freq in lst:
                heappush(h, freq)
            if k != 0 and len(h) != 0:
                cnt += k
        return cnt






class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for task in tasks:
            if task not in dic:
                dic[task] = 0
            dic[task] += 1
        
        freqs = list(dic.values())
        max_freq = max(freqs)
        num_max_freq = freqs.count(max_freq)
        
        return max(len(tasks), (n + 1) * (max_freq - 1) + num_max_freq
