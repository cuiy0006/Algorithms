class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        helper(res, nums, 0);
        return res;
    }
private:
    void helper(vector<vector<int>>& res, vector<int>& curr, int m) {
        if(m == curr.size()){
            res.push_back(curr);
            return;
        }
        
        for(int i = m; i < curr.size(); ++i){
            int tmp = curr[m];
            curr[m] = curr[i];
            curr[i] = tmp;
            helper(res, curr, m + 1);
            curr[i] = curr[m];
            curr[m] = tmp;
        }
    }
};
