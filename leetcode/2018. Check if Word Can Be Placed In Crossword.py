class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rev_word = word[::-1]
        
        m = len(board)
        n = len(board[0])
        
        def check_row(x, y):
            if y > 0 and board[x][y-1] != '#':
                return False
            
            for w in [word, rev_word]:
                i = y
                j = 0
                while i < n and j < len(w):
                    if board[x][i] == ' ' or w[j] == board[x][i]:
                        i += 1
                        j += 1
                    else:
                        break
                if j == len(w) and (i == n or board[x][i] == '#'):
                    return True
            return False


        def check_col(x, y):
            if x > 0 and board[x-1][y] != '#':
                return False

            for w in [word, rev_word]:
                i = x
                j = 0
                while i < m and j < len(w):
                    if board[i][y] == ' ' or w[j] == board[i][y]:
                        i += 1
                        j += 1
                    else:
                        break

                if j == len(w) and (i == m or board[i][y] == '#'):
                    return True
            return False
            

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    continue
                if check_row(i, j) or check_col(i, j):
                    return True
        
        return False
        
        
