class Solution {
public:
    int trap(vector<int>& height) {
        int left_max = 0;
        int right_max = 0;
        int i = 0;
        int j = height.size() - 1;
        int res = 0;
        while(i < j){
            while(i < j && height[i] < height[j]){
                left_max = max(left_max, height[i]);
                res += min(left_max, height[j]) - height[i];
                ++i;
            }
            
            while(i < j && height[i] >= height[j]){
                right_max = max(right_max, height[j]);
                res += min(right_max, height[i]) - height[j];
                --j;
            }
        }
        return res;
    }
};
