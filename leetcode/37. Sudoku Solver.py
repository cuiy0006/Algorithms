class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        rows = [set() for _ in range(m)]
        cols = [set() for _ in range(n)]
        blocks = defaultdict(set)
        
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                s = set()
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        blocks[(x, y)] = s
        empty = []
        
        for i in range(m):
            for j in range(n):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    blocks[(i, j)].add(board[i][j])
                else:
                    empty.append((i, j))
        
        def helper():
            if len(empty) == 0:
                return True
            
            x, y = empty.pop()
            for i in range(1, 10):
                num = str(i)
                if num not in rows[x] and num not in cols[y] and num not in blocks[(x, y)]:
                    board[x][y] = num
                    rows[x].add(num)
                    cols[y].add(num)
                    blocks[(x, y)].add(num)
                    if helper():
                        return True
                    board[x][y] = '.'
                    rows[x].remove(num)
                    cols[y].remove(num)
                    blocks[(x, y)].remove(num)
            empty.append((x, y))
            return False
            
        helper()
            
        
        
