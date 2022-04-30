from collections import deque
import sys

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_len = len(nums)
        nums = nums + nums[:-1]
        sum_arr = [0]
        curr = 0
        for num in nums:
            curr += num
            sum_arr.append(curr)
        
        res = nums[0]
        q = deque([0])
        for i in range(1, len(sum_arr)):
            if i - q[0] >= max_len+1:
                q.popleft()
            
            res = max(res, sum_arr[i] - sum_arr[q[0]])
            
            while len(q) != 0 and sum_arr[i] <= sum_arr[q[-1]]:
                q.pop()
            q.append(i)
        
        return res
            
        
        
 
