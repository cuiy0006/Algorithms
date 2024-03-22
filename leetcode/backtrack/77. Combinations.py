class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(i, nums):
            if len(nums) == k:
                res.append(nums[:])
                return
            if i > n:
                return
            helper(i+1, nums)
            nums.append(i)
            helper(i+1, nums)
            nums.pop()
        
        helper(1, [])
        return res
