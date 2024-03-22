class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        x_set = [set() for _ in range(9)]
        y_set = [set() for _ in range(9)]
        squares = {}

        for x0, x1 in [(0, 3), (3, 6), (6, 9)]:
            for y0, y1 in [(0, 3), (3, 6), (6, 9)]:
                s = set()
                for x in range(x0, x1):
                    for y in range(y0, y1):
                        squares[(x, y)] = s

        blanks = []
        for x in range(9):
            for y in range(9):
                if board[x][y] != '.':
                    x_set[x].add(board[x][y])
                    y_set[y].add(board[x][y])
                    squares[(x, y)].add(board[x][y])
                else:
                    blanks.append((x, y))

        def helper(idx, val):
            if idx > len(blanks)-1:
                return True
            x, y = blanks[idx]
            if val in x_set[x] or val in y_set[y] or val in squares[(x, y)]:
                return False
            board[x][y] = val
            x_set[x].add(val)
            y_set[y].add(val)
            squares[(x, y)].add(val)
            for next_val in range(1, 10):
                if helper(idx+1, str(next_val)):
                    return True
            board[x][y] = '.'
            x_set[x].remove(val)
            y_set[y].remove(val)
            squares[(x, y)].remove(val)
            return False

        for val in range(1, 10):
            if helper(0, str(val)):
                return
        return


            