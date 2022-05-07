class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        res = 0
        
        while i < len(colors):
            j = i + 1
            max_cost = neededTime[i]
            max_idx = i
            while j < len(colors) and colors[j] == colors[j-1]:
                if neededTime[j] > max_cost:
                    max_idx = j
                    max_cost = neededTime[j]
                j += 1
            
            if j != i + 1:
                res += sum([neededTime[x] for x in range(i, j) if x != max_idx])
            i = j
        
        return res
