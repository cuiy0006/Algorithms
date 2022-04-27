from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        
        for i, num in enumerate(nums):
            if len(q) != 0 and i - q[0] >= k:
                q.popleft()
            
            while len(q) != 0 and nums[q[-1]] <= num:
                q.pop()
            
            q.append(i)
            if i >= k - 1:  
                res.append(nums[q[0]])
        
        return res
