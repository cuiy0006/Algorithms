class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def helper(idx, curr, target):
            if target == 0:
                res.append(curr[:])
                return
            if idx == len(candidates) or target < 0:
                return

            end = idx + 1
            while end < len(candidates) and candidates[end] == candidates[end-1]:
                end += 1
            helper(end, curr, target)
            for i in range(idx, end):
                curr.append(candidates[idx])
                target -= candidates[idx]
                helper(end, curr, target)
                if target < 0:
                    break
            while len(curr) != 0 and curr[-1] == candidates[idx]:
                curr.pop()

        helper(0, [], target)
        return res
