class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res = nums;
        for(int i = 0; i < nums.size(); ++i){
            if(i == 0){
                res[i] = nums[i];
            } else {
                res[i] = res[i - 1] * nums[i];
            }
        }
        int curr = 1;
        for(int i = nums.size() - 1; i >= 0; --i){
            if(i == 0){
                res[i] = curr;
                continue;
            }
            res[i] = curr * res[i - 1]; 
            curr *= nums[i];
        }
        return res;
    }
};
