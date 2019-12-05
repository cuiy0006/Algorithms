class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if(m == 0){
            return 0;
        }
        int n = matrix[0].size();
        vector<vector<int>> distances(matrix);
        for(int i = 0; i < m; ++i){
            for(int j = 0; j < n; ++j){
                distances[i][j] = -1;
            }
        }
        int res = 0;
        for(int i = 0; i < m; ++i){
            for(int j = 0; j < n; ++j){
                res = max(res, helper(i, j, INT_MIN, distances, matrix));
            }
        }
        return res;
        
    }
private:
    int helper(int x, int y, int last, vector<vector<int>>& distances, const vector<vector<int>>& matrix){
        int m = matrix.size();
        int n = matrix[0].size();
        if(x < 0 || y < 0 || x >= m || y >= n || matrix[x][y] <= last){
            return 0;
        }
        if(distances[x][y] != -1){
            return distances[x][y];
        }
        
        int left = helper(x - 1, y, matrix[x][y], distances, matrix);
        int right = helper(x + 1, y, matrix[x][y], distances, matrix);
        int up = helper(x, y - 1, matrix[x][y], distances, matrix);
        int down = helper(x, y + 1, matrix[x][y], distances, matrix);
    
        distances[x][y] = 1 + max({left, right, up, down});
        return distances[x][y];
    }
};
