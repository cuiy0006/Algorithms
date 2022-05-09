class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        k = len(costs[0])
        dp1 = [0] * k
        dp2 = [0] * k
        smallest1 = [0] * 2
        smallest2 = [sys.maxsize] * 2
        for cost in costs:
            for i in range(k):
                if dp1[i] == smallest1[1]:
                    dp2[i] = cost[i] + smallest1[0]
                else:
                    dp2[i] = cost[i] + smallest1[1]

                if dp2[i] <= smallest2[1]:
                    smallest2[0] = smallest2[1]
                    smallest2[1] = dp2[i]
                elif dp2[i] < smallest2[0]:
                    smallest2[0] = dp2[i]
                
            dp1 = dp2
            dp2 = [0] * k
            smallest1 = smallest2
            smallest2 = [sys.maxsize] * 2
            
        return min(dp1)
