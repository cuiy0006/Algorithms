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
