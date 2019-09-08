class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end(), [](int a, int b){
            return a > b;
        });
        return nums[k - 1];
    }
};
