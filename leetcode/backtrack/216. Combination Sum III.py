class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def helper(idx, curr, target):
            if target == 0 and len(curr) == k:
                res.append(curr[:])
                return
            if idx > 9 or target < 0 or len(curr) == k:
                return
            helper(idx+1, curr, target)
            curr.append(idx)
            helper(idx+1, curr, target-idx)
            curr.pop()
        
        helper(1, [], n)
        return res
