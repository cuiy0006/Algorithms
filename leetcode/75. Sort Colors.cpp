class Solution {
public:
    void sortColors(vector<int>& nums) {
        int i = 0;
        int k = 0;
        int j = nums.size() - 1;
        while (k <= j) {
            if (nums[k] == 0) {
                std::swap(nums[i], nums[k]);
                i++;
                k++;
            } else if (nums[k] == 2) {
                std::swap(nums[j], nums[k]);
                j--;
            } else {
                k++;
            }
        }
    }
};


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
            
            std::swap(nums[i], nums[j]);
        }
        
        j = nums.size() - 1;
        while(i < j){
            while(i < j && nums[i] == 1){
                ++i;
            }
            
            while(i < j && nums[j] != 1){
                --j;
            }
            std::swap(nums[i], nums[j]);
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
