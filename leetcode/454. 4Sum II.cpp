class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        unordered_map<int, int> map;
        int size = A.size();
        int res = 0;
        for(auto a: A){
            for(auto b: B){
                ++map[a + b];
            }
        }
        
        for(auto c: C){
            for(auto d: D){
                res += map[-(c + d)];
            }
        }
        return res;
    }
};
