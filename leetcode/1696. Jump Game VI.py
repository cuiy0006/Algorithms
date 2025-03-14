class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        res = [-sys.maxsize] * len(nums)
        res[0] = nums[0]
        dq = deque()
        for i in range(len(nums)):
            while len(dq) != 0 and i > dq[0]+k:
                dq.popleft()
            if len(dq) != 0:
                res[i] = max(res[i], res[dq[0]]+nums[i])
            while len(dq) != 0 and res[i] >= res[dq[-1]]:
                dq.pop()
            dq.append(i)
        return res[-1]

