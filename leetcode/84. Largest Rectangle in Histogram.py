class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        
        rst = 0
        for i in range(len(heights) + 1):
            if i == len(heights):
                h = -1
            else:
                h = heights[i]

            while stack and heights[stack[-1]] > h:
                top_idx = stack.pop()
                left_idx = stack[-1] if stack else -1
                rst = max(rst, (i - left_idx - 1) * heights[top_idx])
			
            stack.append(i)
        return rst
            
