class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(prices)-1, -1, -1):
            while len(stack) != 0 and prices[i] < stack[-1]:
                stack.pop()
            if len(stack) == 0:
                res.append(prices[i])
            else:
                res.append(prices[i]-stack[-1])
            stack.append(prices[i])
        res.reverse()
        return res
