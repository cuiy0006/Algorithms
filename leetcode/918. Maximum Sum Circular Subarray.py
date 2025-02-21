class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        circular = nums + nums[:-1]
        presum = []
        curr = 0
        for num in circular:
            curr += num
            presum.append(curr)
        res = max(nums)
        dq = deque()
        for i in range(len(presum)):
            while len(dq) != 0 and i-dq[0] > len(nums):
                dq.popleft()
            while len(dq) != 0 and presum[i] <= presum[dq[-1]]:
                dq.pop()
            if len(dq) != 0:
                res = max(res, presum[i]-presum[dq[0]])
            dq.append(i)
        return res



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
            
        
        
 
