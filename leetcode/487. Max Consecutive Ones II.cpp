class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int s00 = nums[0]; // not do
        int s01 = 1; // do
        
        int s10 = 0; // not do
        int s11 = 0; // do
        
        int res = 1;
        
        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] == 0) {
                s10 = 0;
                s11 = s00 + 1;
            } else {
                s10 = s00 + 1;
                s11 = s01 + 1;
            }
            s00 = s10;
            s01 = s11;
            
            res = max({res, s00, s01});
        }
        
        return res;
        
    }
};
