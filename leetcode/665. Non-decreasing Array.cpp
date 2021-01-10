class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int idx = -1;
        for(size_t i = 0; i < nums.size() - 1; ++i){
            if(nums[i] > nums[i + 1]){
                if(idx != -1){
                    return false;
                }
                
                idx = i;
            }
        }
        
        if(idx == -1 || idx == 0 || idx == nums.size() - 2){
            return true;
        }
        
        if(nums[idx + 1] >= nums[idx - 1] || nums[idx + 2] >= nums[idx]){
            return true;
        }
        
        return false;
    }
};
