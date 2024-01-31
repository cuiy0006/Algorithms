class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for [a, b] in prerequisites:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
        
        visited = set()
        on_path = set()
        res = []

        def traverse(course):
            if course in on_path:
                return False
            if course in visited:
                return True
            visited.add(course)
            on_path.add(course)

            if course in graph:
                for p in graph[course]:
                    if not traverse(p):
                        return False
            
            on_path.remove(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not traverse(course):
                return []

        return res

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        deps = defaultdict(list)
        for [a, b] in prerequisites:
            indegree[a] += 1
            deps[b].append(a)
        
        no_deps = []
        for course in range(numCourses):
            if indegree[course] == 0:
                no_deps.append(course)

        done = []
        while len(no_deps) != 0:
            course = no_deps.pop()
            done.append(course)
            for dep in deps[course]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    no_deps.append(dep)

        return done if len(done) == numCourses else []
