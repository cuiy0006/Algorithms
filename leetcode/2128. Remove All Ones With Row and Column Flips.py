class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        row0 = grid[0]
        row0r = [1-e for e in row0]
        
        for i in range(1, len(grid)):
            if grid[i] != row0 and grid[i] != row0r:
                return False
        
        return True
