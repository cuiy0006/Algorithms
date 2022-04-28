class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        
        rotated = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                rotated[j][m-i-1] = box[i][j]
                
        for j in range(m):
            a = b = n - 1
            while b >= 0:
                if rotated[b][j] == '#':
                    rotated[a][j], rotated[b][j] = rotated[b][j], rotated[a][j]
                    a -= 1
                elif rotated[b][j] == '*':
                    a = b - 1
                b -= 1
        
        return rotated
