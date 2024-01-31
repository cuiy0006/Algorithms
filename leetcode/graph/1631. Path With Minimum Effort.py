class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        h = []
        heappush(h, (0, 0, 0)) # effort, x, y
        visited = {}
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        print(heights, len(heights))

        while len(h) != 0:
            effort, x, y = heappop(h)
            if x == len(heights)-1 and y == len(heights[0])-1:
                return effort
            if (x, y) in visited and visited[(x, y)] <= effort:
                continue
            visited[(x, y)] = effort
            for d in dirs:
                x0 = x + d[0]
                y0 = y + d[1]
                if x0 >= 0 and x0 < len(heights) and y0 >= 0 and y0 < len(heights[0]):
                    heappush(h, 
                        (max(effort, abs(heights[x][y] - heights[x0][y0])), x0, y0))
        return visited[(len(heights)-1, len(heights[0])-1)]
        
