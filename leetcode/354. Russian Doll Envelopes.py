class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        matches = {}
        
        def helper(boy, seen):
            for girl in range(n):
                if grid[boy][girl] == 0:
                    continue
                
                if girl in seen:
                    continue
                seen.add(girl)
                
                if girl not in matches or helper(matches[girl], seen):
                    matches[girl] = boy
                    return True
            return False
        
        for boy in range(m):
            helper(boy, set())
        
        return len(matches)
