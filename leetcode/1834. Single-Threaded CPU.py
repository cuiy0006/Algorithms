from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        tasks.sort(key=lambda task:task[0])
        
        curr = tasks[0][0]
        h = []
        res = []
        
        i = 0
        while i < len(tasks):
            j = i
            while j < len(tasks):
                if tasks[j][0] <= curr:
                    heappush(h, (tasks[j][1], tasks[j][2]))
                    j += 1
                else:
                    break
            
            print(i)

            if len(h) != 0:
                processing, idx = heappop(h)
                res.append(idx)
                curr += processing
            else:
                if i != len(tasks):
                    curr = tasks[i][0]
            i = j
        
        while len(h) != 0:
            _, idx = heappop(h)
            res.append(idx)
        
        return res
