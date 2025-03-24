class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = {}
        for [a, b] in prerequisites:
            if a not in dic:
                dic[a] = []
            dic[a].append(b)
        
        seen = set()
        onpath = set()
        res = []
        def can_finish(course):
            if course in onpath:
                return False
            if course in seen:
                return True 
            seen.add(course)
            if course not in dic:
               res.append(course)
               return True
            onpath.add(course)
            for dep in dic[course]:
                if not can_finish(dep):
                    return False
            onpath.remove(course)
            res.append(course)
            return True

        for course in range(0, numCourses):
            if not can_finish(course):
                return []
        return res
