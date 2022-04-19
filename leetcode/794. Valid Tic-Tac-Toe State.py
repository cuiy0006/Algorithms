class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # o_win == True and x_win == True --> impossible
        # o_win == True --> num_x == num_o
        # x_win == True --> num_x - num_o == 1
        # 1 >= num_x - num_o >= 0
        
        num_x = 0
        num_o = 0
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        rev_diag = 0
        
        x_win = False
        o_win = False
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'X':
                    num_x += 1
                    incr = 1
                elif board[x][y] == 'O':
                    num_o += 1
                    incr = -1
                else:
                    continue
                
                rows[x] += incr
                if rows[x] == 3:
                    if o_win:
                        return False
                    x_win = True
                elif rows[x] == -3:
                    if x_win:
                        return False
                    o_win = True
                
                cols[y] += incr
                if cols[y] == 3:
                    if o_win:
                        return False
                    x_win = True
                elif cols[y] == -3:
                    if x_win:
                        return False
                    o_win = True
                
                
                if x == y:
                    diag += incr
                    if diag == 3:
                        if o_win:
                            return False
                        x_win = True
                    elif diag == -3:
                        if x_win:
                            return False
                        o_win = True
                        
                if x + y == 2:
                    rev_diag += incr
                    if rev_diag == 3:
                        if o_win:
                            return False
                        x_win = True
                    elif rev_diag == -3:
                        if x_win:
                            return False
                        o_win = True

        if x_win:
            if num_x - num_o != 1:
                return False
        if o_win:
            if num_x != num_o:
                return False
        
        if num_x < num_o:
            return False
        if num_x - num_o > 1:
            return False
        return True
                    
                    
                
                
