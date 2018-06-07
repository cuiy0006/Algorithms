from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res =[]
        q = deque()
        for i, num in enumerate(nums):
            if len(q) > 0 and i - q[0] == k:
                q.popleft()
            while len(q) > 0 and num >= nums[q[-1]]:
                q.pop()
            q.append(i)
            if i >= k -1:
                res.append(nums[q[0]])
        return res
