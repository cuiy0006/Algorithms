class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        res = 0
        i = 0
        while i < len(s):
            j = i + 1
            last_cost = cost[i]
            while j < len(s):
                if s[i] == s[j]:
                    if last_cost < cost[j]:
                        res += last_cost
                        last_cost = cost[j]
                    else:
                        res += cost[j]
                else:
                    break
                j += 1
            i = j
        return res
