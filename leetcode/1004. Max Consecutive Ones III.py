class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        q = deque()
        left = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] != 1:
                if k == 0:
                    left = i + 1
                elif len(q) != k:
                    q.append(i)
                else:
                    left = q.popleft() + 1
                    q.append(i)

            res = max(res, i - left + 1)

        return res
