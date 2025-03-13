class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i in range(len(nums)):
            while len(dq) != 0 and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            while len(dq) != 0 and i - dq[0] >= k:
                dq.popleft()
            if i >= k-1:
                res.append(nums[dq[0]])
        return res

