class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        
        for seq in sequences:
            if seq[0] not in indegree:
                indegree[seq[0]] = 0
            for i in range(1, len(seq)):
                indegree[seq[i]] += 1
                graph[seq[i-1]].append(seq[i])

        q = deque()
        for num, degree in indegree.items():
            if degree == 0:
                q.append(num)
                
        minimum = []
        while len(q) != 0:
            if len(q) != 1:
                return False
            num = q.popleft()
            minimum.append(num)
            for other in graph[num]:
                indegree[other] -= 1
                if indegree[other] == 0:
                    q.append(other)
                    print('in: ' + str(other))
        
        return minimum == nums
                
