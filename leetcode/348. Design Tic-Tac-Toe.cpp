class TicTacToe {
public:
    /** Initialize your data structure here. */
    TicTacToe(int n)
        : rows(vector(n, 0)),
          cols(vector(n, 0)),
          diag(0),
          rev_diag(0),
          n(n){
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    int move(int row, int col, int player) {
        int val = player == 1? 1: -1;
        rows[row] += val;
        cols[col] += val;
        if(row == col){
            diag += val;
        }
        if(row + col == n - 1){
            rev_diag += val;
        }
        if(abs(rows[row]) == n || abs(cols[col]) == n || abs(diag) == n || abs(rev_diag) == n){
            return player;
        }
        return 0;
    }

private:
    vector<int> rows;
    vector<int> cols;
    int diag;
    int rev_diag;
    int n;
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */
