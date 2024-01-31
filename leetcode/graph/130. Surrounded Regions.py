class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i != 0 and i != len(board)-1 and j != 0 and j != len(board[0])-1:
                    continue
                if board[i][j] != 'O':
                    continue
                q = deque([(i, j)])
                while len(q) != 0:
                    x, y = q.popleft()
                    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                        continue
                    if board[x][y] != 'O':
                        continue
                    board[x][y] = 'V'
                    q.append((x+1, y))
                    q.append((x-1, y))
                    q.append((x, y-1))
                    q.append((x, y+1))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'V':
                    board[i][j] = 'O'




