class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int x[] = {-1, -1, -1, 0, 0, 1, 1, 1};
        int y[] = {0, 1, -1, 1, -1, 0, 1, -1};
        for(int i = 0; i < board.size(); ++i){
            for(int j = 0; j < board[i].size(); ++j){
                int lives = 0;
                for(int m = 0; m < 8; ++m){
                    int x0 = x[m] + i;
                    int y0 = y[m] + j;
                    if(x0 < 0 || x0 > board.size() - 1 || y0 < 0 || y0 > board[i].size() - 1){
                        continue;
                    }
                    lives += isAlive(board[x0][y0]);
                }

                if(board[i][j] == 1 && lives < 2){
                    board[i][j] = 2;
                } else if(board[i][j] == 1 && (lives == 2 || lives == 3)){
                    board[i][j] = 3;
                } else if(board[i][j] == 1 && lives > 3){
                    board[i][j] = 4;
                } else if(board[i][j] == 0 && lives == 3) {
                    board[i][j] = 5;
                } else {
                    board[i][j] = 0;
                }
            }
        }
        
        for(int i = 0; i < board.size(); ++i){
            for(int j = 0; j < board[i].size(); ++j){
                if(board[i][j] == 2 || board[i][j] == 4){
                    board[i][j] = 0;
                } else if(board[i][j] == 3 || board[i][j] == 5) {
                    board[i][j] = 1;
                }
            }   
        }
    }
    
private:
    int isAlive(int val){
        return val == 2 || val == 3 || val == 4 || val == 1? 1 : 0;
    }
};
