class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        right = -float('inf')
        stack = []
        
        i = len(nums) - 1
        while i >= 0:
            num = nums[i]
            if right > num:
                return True
            
            while len(stack) != 0 and num > stack[-1]:
                right = stack.pop()
            
            stack.append(num)
            i -= 1
            
        return False
