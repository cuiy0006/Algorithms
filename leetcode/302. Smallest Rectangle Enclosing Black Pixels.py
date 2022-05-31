class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m = len(image)
        n = len(image[0])
        min_x = m-1
        min_y = n-1
        max_x = 0
        max_y = 0
        
        for i in range(m):
            for j in range(n):
                if image[i][j] == '1':
                    min_x = min(min_x, i)
                    max_x = max(max_x, i)
                    min_y = min(min_y, j)
                    max_y = max(max_y, j)
        
        return (max_y-min_y+1) * (max_x-min_x+1)

