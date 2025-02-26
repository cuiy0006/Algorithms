class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(start):
            if start == len(nums):
                res.append(nums[:])
                return

            seen = set()
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                nums[i], nums[start] = nums[start], nums[i]
                helper(start+1)
                nums[i], nums[start] = nums[start], nums[i]
        
        helper(0)
        return res
