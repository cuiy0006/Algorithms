class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> curr;
        vector<vector<int>> res;
        helper(res, curr, nums, 0);
        return res;
    }
private:
    void helper(vector<vector<int>>& res, vector<int>& curr, vector<int>& nums, int index){
        res.push_back(curr);

        for(int i = index; i < nums.size(); ++i){
            curr.push_back(nums[i]);
            helper(res, curr, nums, i + 1);
            curr.pop_back();
        }
    }
};
