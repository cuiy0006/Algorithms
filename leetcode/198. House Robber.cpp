class Solution {
public:
    int rob(vector<int>& nums) {
        int this_rob = nums[0];
        int this_not_rob = 0;

        for (size_t i = 1; i < nums.size(); i++) {
            int last_rob = this_rob;
            int last_not_rob = this_not_rob;
            this_rob = last_not_rob + nums[i];
            this_not_rob = max(last_rob, last_not_rob);

        }

        return max(this_rob, this_not_rob);
    }
};
