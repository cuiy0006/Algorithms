from heapq import heappush, heappop

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        h = [(-nums[0], 0)]
        
        for i in range(1, len(nums)):
            while True:
                neg_num, idx = h[0]
                if i - idx <= k:
                    dp[i] = nums[i] - neg_num
                    break
                else:
                    heappop(h)
            
            heappush(h, (-dp[i], i))

        return dp[-1]
