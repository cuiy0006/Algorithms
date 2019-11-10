class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_max = 0
        i = 0
        while i <= curr_max:
            curr_max = max(curr_max, i + nums[i])
            if curr_max >= len(nums) - 1:
                return True
            i += 1
        return False
