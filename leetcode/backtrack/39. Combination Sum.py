class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(idx, curr, target):
            if target == 0:
                res.append(curr[:])
                return
            if idx == len(candidates) or target < 0:
                return
            helper(idx+1, curr, target)
            while target >= 0:
                target -= candidates[idx]
                curr.append(candidates[idx])
                helper(idx+1, curr, target)

            while len(curr) != 0 and curr[-1] == candidates[idx]:
                curr.pop()
        helper(0, [], target)
        return res
