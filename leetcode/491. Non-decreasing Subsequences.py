class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr, idx):
            if len(curr) >= 2:
                res.append(curr[:])
            if idx == len(nums):
                return

            seen = set()
            for i in range(idx, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                if len(curr) == 0 or curr[-1] <= nums[i]:
                    curr.append(nums[i])
                    dfs(curr, i+1)
                    curr.pop()
        dfs([], 0)
        return res
