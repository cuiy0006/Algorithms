#LTE
from heapq import heappush
from heapq import heappop
from collections import deque
d = ((0,1), (1,0), (0,-1), (-1,0))

class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        def helper(start_x, start_y, x, y):
            q = deque([(start_x, start_y)])
            visited = [[False for i in range(len(forest[0]))] for j in range(len(forest))]
            visited[start_x][start_y] = True
            step = 0
            
            while len(q) != 0:
                size = len(q)
                while size != 0:
                    m, n = q.popleft()
                    size -= 1
                    if m == x and n == y:
                        return step
                    for inc_x, inc_y in d:
                        new_x, new_y = m + inc_x, n + inc_y
                        if new_x < 0 or new_x > len(forest) -1 or new_y < 0 or new_y > len(forest[0]) -1 or forest[new_x][new_y] == 0 or visited[new_x][new_y]:
                            continue
                        visited[new_x][new_y] = True
                        q.append((new_x, new_y))
                step += 1
                        
            return -1
        
        res = 0
        h = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] != 0:
                    heappush(h, (forest[i][j], i, j))
        
        start = [0, 0]
        while len(h) != 0:
            height, x, y = heappop(h)
            curr = helper(start[0], start[1], x, y)
            if curr == -1:
                return -1
            res += curr
            start[0], start[1] = x, y
        return res



#improved
