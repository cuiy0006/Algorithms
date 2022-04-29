class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        
        for i, height in enumerate(heights):
            while len(stack) != 0 and heights[stack[-1]] <= height:
                stack.pop()
            
            stack.append(i)
        
        return stack
