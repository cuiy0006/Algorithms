class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        prev_larger = [-1] * n
        next_larger = [n] * n
        stack = []
        for i, num in enumerate(nums):
            while len(stack) != 0 and nums[stack[-1]] < num:
                next_larger[stack[-1]] = i
                stack.pop()
            
            if len(stack) != 0:
                prev_larger[i] = stack[-1]
            stack.append(i)
        
        prev_smaller = [-1] * n
        next_smaller = [n] * n
        stack = []
        for i, num in enumerate(nums):
            while len(stack) != 0 and nums[stack[-1]] > num:
                next_smaller[stack[-1]] = i
                stack.pop()
            
            if len(stack) != 0:
                prev_smaller[i] = stack[-1]
            stack.append(i)
        
        res = 0
        for i in range(len(nums)):
            res -= nums[i] * (i - prev_smaller[i]) * (next_smaller[i] - i)
            res += nums[i] * (i - prev_larger[i]) * (next_larger[i] - i)
        return res
        
