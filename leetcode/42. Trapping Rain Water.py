class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        
        res = 0
        left_max = 0
        right_max = 0
        
        while i < j:
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[j])
            
            while i < j and height[i] < height[j]:
                i += 1
                left_max = max(left_max, height[i])
                res += left_max - height[i]
            
            while i < j and height[i] >= height[j]:
                j -= 1
                right_max = max(right_max, height[j])
                res += right_max - height[j]
        
        return res



class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while len(stack) != 0 and height[i] >= height[stack[-1]]:
                idx = stack.pop()
                if len(stack) != 0:
                    w = (i-stack[-1]-1)
                    h = min(height[i], height[stack[-1]]) - height[idx]
                    res += w * h
            stack.append(i)
        return res
