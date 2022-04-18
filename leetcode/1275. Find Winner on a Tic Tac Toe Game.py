class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0, 0, 0]
        cols = [0, 0, 0]
        diag = 0
        rev_diag = 0
        
        for i, [x, y] in enumerate(moves):
            if i % 2 == 0:
                rows[x] += 1
                cols[y] += 1
                if x == y:
                    diag += 1
                if x + y == 2:
                    rev_diag += 1
                
                if rows[x] == 3 or cols[y] == 3 or diag == 3 or rev_diag == 3:
                    return 'A'
            else:
                rows[x] -= 1
                cols[y] -= 1
                if x == y:
                    diag -= 1
                if x + y == 2:
                    rev_diag -= 1
                    
                if rows[x] == -3 or cols[y] == -3 or diag == -3 or rev_diag == -3:
                    return 'B'
        
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'
