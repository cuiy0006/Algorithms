class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dic = {}
        for course, pre in prerequisites:
            if course not in dic:
                dic[course] = [pre]
            else:
                dic[course].append(pre)
        res = []
        taken = set()
        def helper(visited, course):
            if course in taken:
                return True
            if course in visited:
                return False
            visited.add(course)
            if course in dic:
                for pre in dic[course]:
                    if not helper(visited, pre):
                        return False
            taken.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not helper(set(), course):
                return []
        return res
