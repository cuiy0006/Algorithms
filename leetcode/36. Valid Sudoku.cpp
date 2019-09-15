class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i = 0; i < 9; ++i){
            if(!isValid(board, i, true) || !isValid(board, i, false)){
                return false;
            }
        }
        
        for(int i = 0; i < 3; ++i){
            for(int j = 0; j < 3; ++j){
                if(!isSquareValid(board, 3 * i, 3 * j)){
                    return false;
                }
            }
        }
        return true;
    }

private:
    bool isValid(vector<vector<char>>& board, int j, int isRow){
        set<char> s;
        for(int i = 0; i < 9; ++i){
            char c = isRow? board[j][i]: board[i][j];
            if(c == '.'){
                continue;
            }
            if(s.find(c) != s.end()){
                return false;
            }
            s.emplace(c);
        }
        return true;
    }
    
    bool isSquareValid(vector<vector<char>>& board, int x, int y){
        set<char> s;
        for(int i = x; i < x + 3; ++i){
            for(int j = y; j < y + 3; ++j){
                char c = board[i][j];
                if(c == '.'){
                    continue;
                }
                if(s.find(c) != s.end()){
                    return false;
                }
                s.emplace(c);
            }
        }
        return true;
    }
    
};
