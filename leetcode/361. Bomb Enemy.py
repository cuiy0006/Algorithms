class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        positions = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            k = 0
            j = 0
            while j < n:
                enemy = 0
                while j < n:
                    if grid[i][j] == 'W':
                        break
                    elif grid[i][j] == 'E':
                        enemy += 1
                    j += 1

                while k < j:
                    positions[i][k] += enemy
                    k += 1

                k += 1
                j += 1

        for j in range(n):
            k = 0
            i = 0
            while i < m:
                enemy = 0
                while i < m:
                    if grid[i][j] == 'W':
                        break
                    elif grid[i][j] == 'E':
                        enemy += 1
                    i += 1
                
                while k < i:
                    positions[k][j] += enemy
                    k += 1
                k += 1
                i += 1
        
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 'W' and grid[i][j] != 'E':
                    res = max(res, positions[i][j])
        
        return res
