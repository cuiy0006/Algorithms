class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        
        res = []
        seen = set()
        
        for [x, y] in adjacentPairs:
            dic[x].append(y)
            dic[y].append(x)
        
        sides = []
        
        for x, neighbours in dic.items():
            if len(neighbours) == 1:
                sides.append(x)
        
        start = sides[0]
        end = sides[1]
        
        def helper(curr):
            if curr in seen:
                return
            seen.add(curr)
            
            res.append(curr)
            if curr == end:
                return
            
            for neighbour in dic[curr]:
                helper(neighbour)
        
        helper(start)
        return res
            
            
            
        
