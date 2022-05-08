from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        num_to_idx = {}
        n = len(board)
        reverse = False
        start = None
        
        num = 1
        for i in range(n-1, -1, -1):
            if reverse:
                for j in range(n-1, -1, -1):
                    num_to_idx[num] = (i, j)
                    num += 1
            else:
                for j in range(0, n):
                    num_to_idx[num] = (i, j)
                    num += 1
            reverse = not reverse

        q = deque([(n-1, 0, 1)])
        d = 0
        target = n * n
        visited = set()
        
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                x, y, num = q.popleft()
                if num == target:
                    return d
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                
                for i in range(num+1, min(num+6, target)+1):
                    x0, y0 = num_to_idx[i]
                    if board[x0][y0] != -1:
                        x1, y1 = num_to_idx[board[x0][y0]]
                        q.append((x1, y1, board[x0][y0]))
                    else:
                        q.append((x0, y0, i))
            d += 1
        
        return -1
