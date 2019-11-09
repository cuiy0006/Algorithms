from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {}
        for first, second in prerequisites:
            if first not in dic:
                dic[first] = [second]
            else:
                dic[first].append(second)
         
        seen = set()
        p_seen = set()
        def dfs(i, p_seen):
            if i in p_seen:
                return False
            if i in seen:
                return True
            p_seen.add(i)
            if i in dic:    
                for j in dic[i]:
                    if not dfs(j, p_seen):
                        return False
            p_seen.remove(i)
            seen.add(i)
            return True
                
        for i in range(numCourses):
            if not dfs(i, p_seen):
                return False
        return True
