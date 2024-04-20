class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        dir1 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        def traverse(x, y):
            if x < 0 or x > len(board)-1 or y < 0 or y > len(board[0])-1:
                return
            if board[x][y] != 'E':
                return
            
            cnt = 0
            for (x0, y0) in dir1:
                x1 = x+x0
                y1 = y+y0
                if x1 < 0 or x1 > len(board)-1 or y1 < 0 or y1 > len(board[0])-1:
                    continue
                if board[x1][y1] == 'M':
                    cnt += 1
            if cnt == 0:
                board[x][y] = 'B'
                for (x0, y0) in dir1:
                    traverse(x+x0, y+y0)
            else:
                board[x][y] = str(cnt)

        traverse(click[0], click[1])
        return board

