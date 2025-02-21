class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(heights)-1, -1, -1):
            cnt = 0
            while len(stack) !=0 and heights[i] > heights[stack[-1]]:
                stack.pop()
                cnt += 1
            if len(stack) != 0:
                cnt += 1
            res.append(cnt)
            stack.append(i)
        res.reverse()
        return res
