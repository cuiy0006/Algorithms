from heapq import heappush, heappop

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        zipped = list(zip(startTime, endTime, profit))
        zipped.sort(key=lambda x: x[0])
        
        h = [] # (end, profit)
        max_p = 0
        
        for i in range(0, len(zipped)):
            start, end, p = zipped[i]
            while len(h) != 0:
                if start < h[0][0]:
                    break
                max_p = max(max_p, heappop(h)[1])
            
            curr_p = max_p + p
            heappush(h, (end, curr_p))
            
        while len(h) != 0:
            max_p = max(max_p, heappop(h)[1])
        
        return max_p



class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        zipped = list(zip(startTime, endTime, profit))
        zipped.sort(key=lambda x: x[1])
        
        dp = [0 for _ in range(len(startTime)+1)]
        max_p = 0
        
        for i in range(1, len(startTime)+1):
            curr_max = 0
            for j in range(1, i):
                if zipped[j-1][1] > zipped[i-1][0]:
                    break
                curr_max = max(curr_max, dp[j])
            dp[i] = curr_max + zipped[i-1][2]
            max_p = max(max_p, dp[i])
            
        return max_p
            
        
        
