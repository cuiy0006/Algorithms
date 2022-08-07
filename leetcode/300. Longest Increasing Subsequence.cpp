class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp;
        
        for (auto num: nums) {
            int i = 0;
            int j = dp.size();
            while (i < j) {
                int mid = (i + j) / 2;
                if (dp[mid] < num) {
                    i = mid + 1;
                } else {
                    j = mid;
                }
            }
            
            if (i == dp.size()) {
                dp.push_back(num);
            } else {
                dp[i] = num;
            }
        }
        
        return dp.size();
    }
};
