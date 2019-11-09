class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = {}
        for first, second in prerequisites:
            if first not in dic:
                dic[first] = [second]
            else:
                dic[first].append(second)
                
        seen = set()
        p_seen = set()
        res = []
        def dfs(i):
            if i in p_seen:
                return False
            if i in seen:
                return True
            p_seen.add(i)
            if i in dic:
                for j in dic[i]:
                    if not dfs(j):
                        return False
            p_seen.remove(i)
            seen.add(i)
            res.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
