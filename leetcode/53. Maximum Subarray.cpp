class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sub = INT_MIN;
        int curr = 0;
        for(auto num: nums){
            curr += num;
            max_sub = max(max_sub, curr);
            if(curr <= 0){
                curr = 0;
            }
        }
        return max_sub;
    }
};
