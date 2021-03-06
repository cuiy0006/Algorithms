class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int i = 0;
        int j = A.size() - 1;
        while(i < j){
            while(i < j && A[i] % 2 == 0){
                ++i;
            }
            while(i < j && A[j] % 2 == 1){
                --j;
            }
            int tmp = A[i];
            A[i] = A[j];
            A[j] = tmp;
        }
        return A;
    }
};
