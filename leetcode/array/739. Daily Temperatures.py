class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        next_greater = [None for _ in temperatures]

        for i in range(len(temperatures)-1, -1, -1):
            while len(stack) != 0 and stack[-1][1] <= temperatures[i]:
                stack.pop()
            if len(stack) == 0:
                next_greater[i] = 0
            else:
                next_greater[i] = stack[-1][0] - i
            stack.append((i, temperatures[i]))
        return next_greater

