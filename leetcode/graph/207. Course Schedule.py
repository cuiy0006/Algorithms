class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for [a, b] in prerequisites:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
        
        visited = set()
        on_path = set()
        def traverse(course):
            if course in on_path:
                return False
            if course in visited:
                return True
            visited.add(course)
            
            if course not in graph:
                return True

            on_path.add(course)
            for p in graph[course]:
                if not traverse(p):
                    return False
            on_path.remove(course)
            return True

        for course in range(numCourses):
            if not traverse(course):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        deps = defaultdict(list)
        for [a, b] in prerequisites:
            indegree[a] += 1
            deps[b].append(a)
        
        no_deps = []
        for course in range(numCourses):
            if indegree[course] == 0:
                no_deps.append(course)

        done = 0
        while len(no_deps) != 0:
            course = no_deps.pop()
            done += 1
            for dep in deps[course]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    no_deps.append(dep)

        return done == numCourses
