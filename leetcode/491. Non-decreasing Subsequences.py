class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(start, curr_lst):
            if len(curr_lst) >= 2:
                res.append(curr_lst[:])
            seen = set()
            for i in range(start, len(nums)):
                if len(curr_lst) != 0 and nums[i] < curr_lst[-1]:
                    continue
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                curr_lst.append(nums[i])
                helper(i+1, curr_lst)
                curr_lst.pop()
        helper(0, [])
        return res
