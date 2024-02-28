class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + nums[:-1]
        next_greater = [None for _ in range(n)]
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while len(stack) != 0 and nums[i] >= stack[-1]:
                stack.pop()
            if i < n:
                if len(stack) == 0:
                    next_greater[i] = -1
                else:
                    next_greater[i] = stack[-1]
            stack.append(nums[i])
        return next_greater
