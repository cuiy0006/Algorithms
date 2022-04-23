class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic = defaultdict(set)
        for i, [first, second] in enumerate(equations):
            factor = values[i]
            dic[first].add((factor, second))
            if factor != 0:
                dic[second].add((1/factor, first))
        
        def find_result(curr, end, seen):
            if curr in seen or curr not in dic:
                return -1
            
            if curr == end:
                return 1
            
            seen.add(curr)
            for [factor, variable] in dic[curr]:
                res = find_result(variable, end, seen)
                if res >= 0:
                    return factor * res
            seen.remove(curr)
            return -1
            
        res = []
        for [begin, end] in queries:
            if end not in dic:
                res.append(-1)
            else:
                res.append(find_result(begin, end, set()))
        
        return res
