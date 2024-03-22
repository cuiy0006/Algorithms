class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def helper(idx, curr):
            if idx == len(nums):
                res.append(curr[:])
                return
            if len(curr) != 0 and nums[idx] == curr[-1]:
                curr.append(nums[idx])
                helper(idx+1, curr)
                curr.pop()
            else:
                helper(idx+1, curr)
                curr.append(nums[idx])
                helper(idx+1, curr)
                curr.pop()

        helper(0, [])
        return res