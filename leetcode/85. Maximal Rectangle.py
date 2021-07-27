class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        
        def max_area(heights):
            stack = []
            res = 0
            heights.append(-1)
            for i, height in enumerate(heights):
                if i != 0:
                    while len(stack) != 0:
                        prev_idx = stack[-1]
                        if height > heights[prev_idx]:
                            break
                        else:
                            stack.pop()
                            prev_prev_idx = -1 if len(stack) == 0 else stack[-1]
                            res = max(res, (i - prev_prev_idx - 1) * heights[prev_idx])
                    
                stack.append(i)
            return res
        
        res = 0
        heights = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heights[j] = 0 if matrix[i][j] == '0' else heights[j] + 1
            res = max(res, max_area(heights[:]))
                
        return res
