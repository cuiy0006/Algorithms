class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = []
        lcurr = height[0]
        for h in height:
            lcurr = max(lcurr, h)
            lmax.append(lcurr)
        
        rmax = []
        rcurr = height[-1]
        for i in range(len(height)-1, -1, -1):
            rcurr = max(rcurr, height[i])
            rmax.append(rcurr)
        rmax.reverse()

        res = 0
        for i in range(len(height)):
            maxh = min(lmax[i], rmax[i])
            if maxh > height[i]:
                res += maxh - height[i]
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while len(stack) != 0 and height[i] >= height[stack[-1]]:
                idx = stack.pop()
                if len(stack) != 0:
                    res += (min(height[stack[-1]], height[i]) - height[idx]) * (i-stack[-1]-1)
            stack.append(i)
        return res


