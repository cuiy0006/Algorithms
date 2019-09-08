class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int i = 0;
        int j = matrix.size() - 1;
        while(i < j){
            for(int m = 0; m < matrix[0].size(); ++m){
                int tmp = matrix[i][m];
                matrix[i][m] = matrix[j][m];
                matrix[j][m] = tmp;
            }
            ++i;
            --j;
        }
        
        for(int m = 0; m < matrix.size(); ++m){
            for(int n = 0; n < m; ++n){
                int tmp = matrix[m][n];
                matrix[m][n] = matrix[n][m];
                matrix[n][m] = tmp;
            }
        }
    }
};
