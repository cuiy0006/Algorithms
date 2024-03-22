class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(idx, curr):
            if idx == len(nums):
                res.append(curr[:])
                return
            helper(idx+1, curr)
            curr.append(nums[idx])
            helper(idx+1, curr)
            curr.pop()
        helper(0, [])
        return res
