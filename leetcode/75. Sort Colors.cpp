class Solution {
public:
    void sortColors(vector<int>& nums) {
        int i = 0;
        int j = nums.size() - 1;
        while(i < j){
            while(i < j && nums[i] == 0){
                ++i;
            }
            
            while(i < j && nums[j] != 0){
                --j;
            }
            
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
        
        j = nums.size() - 1;
        while(i < j){
            while(i < j && nums[i] != 2){
                ++i;
            }
            
            while(i < j && nums[j] != 1){
                --j;
            }
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
    }
};


class Solution {
public:
    void sortColors(vector<int>& nums) {
        int num_zero = 0;
        int num_one = 0;
        for (auto num : nums) {
            if (num == 0) {
                num_zero++;
            } else if (num == 1) {
                num_one++;
            }
        }
        int i = 0;
        while (i < num_zero) {
            nums[i] = 0;
            i++;
        }
        while (i < num_zero + num_one) {
            nums[i] = 1;
            i++;
        }
        while (i < nums.size()) {
            nums[i] = 2;
            i++;
        }
    }
};
