import sys

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        curr_max = next_max = nums[0]
        l = 1
        for i in range(1, len(nums)):
            num = nums[i]
            if num < curr_max:
                l = i + 1
                curr_max = max(curr_max, next_max)
            else:
                next_max = max(next_max, num)
                
        return l
