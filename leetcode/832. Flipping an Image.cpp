class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        for(int i = 0; i < A.size(); ++i){
            int m = 0;
            int n = A[i].size() - 1;
            while(m <= n){
                int tmp = A[i][m];
                A[i][m] = 1 - A[i][n];
                A[i][n] = 1 - tmp;
                ++m;
                --n;
            }
        }
        return A;
    }
};
