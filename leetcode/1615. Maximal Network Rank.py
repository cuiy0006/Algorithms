class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        s = set([(road[0], road[1]) for road in roads])
        ranks = [[i, 0] for i in range(n)]
        
        for road in roads:
            ranks[road[0]][1] += 1
            ranks[road[1]][1] += 1
        
        ranks.sort(key=lambda x:-x[1])
        res = 0
        
        for i in range(len(ranks)):
            for j in range(i + 1, len(ranks)):
                city1 = ranks[i][0]
                city2 = ranks[j][0]
                
                total = ranks[i][1] + ranks[j][1]
                if (city1, city2) in s or (city2, city1) in s:
                    total -= 1
                
                if total < res:
                    break
                else:
                    res = total
        
        return res
            
