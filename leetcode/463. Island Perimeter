class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        def helper(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1
            elif grid[i][j] == 0:
                return 1
            else:
                if visited[i][j]:
                    return 0
                visited[i][j] = True
                return helper(i+1,j) + helper(i-1,j)+helper(i,j+1)+helper(i,j-1)
                
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return helper(i, j)
