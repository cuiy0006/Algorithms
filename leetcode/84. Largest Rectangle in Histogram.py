class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        heights.append(-1)
        
        for i, height in enumerate(heights):
            while len(stack) != 0 and height < heights[stack[-1]]:
                idx = stack.pop()
                if len(stack) == 0:
                    res = max(res, i * heights[idx])
                else:
                    res = max(res, (i-stack[-1]-1) * heights[idx])
            
            stack.append(i)
        
        return res
            
