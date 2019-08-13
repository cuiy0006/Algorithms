class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0;
        int j = 0;
        while(true){
            while(j < nums.size() && nums[j] == 0){
                ++j;
            }
            if(j == nums.size()){
                break;
            }
            nums[i] = nums[j];
            ++i;
            ++j;
        }
        while(i < nums.size()){
            nums[i] = 0;
            ++i;
        }
    }
};
