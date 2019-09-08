class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int left = 1;
        int right = nums.size();
        while(left < right){
            int mid = (left + right) / 2;
            int cnt = 0;

            for(auto num: nums){
                if(num <= mid){
                    ++cnt;
                }
            }
            
            if(cnt > mid){
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
