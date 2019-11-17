class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        heights.append(-1)
        for i, height in enumerate(heights):
            while len(stack) != 0:
                j = stack[-1]
                if height >= heights[j]:
                    break
                stack.pop()
                prev_idx = stack[-1] if len(stack) != 0 else -1 
                res = max(res, (i - prev_idx -1) * heights[j])
            stack.append(i)
        return res
