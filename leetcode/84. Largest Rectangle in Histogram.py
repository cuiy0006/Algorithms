class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(-1)
        res = 0
        for i in range(len(heights)):
            while len(stack) != 0 and heights[i] <= heights[stack[-1]]:
                idx = stack.pop()
                height = heights[idx]
                if len(stack) == 0:
                    width = i
                else:
                    width = (i - stack[-1] - 1)
                
                res = max(res, height * width)
            stack.append(i)

        return res
