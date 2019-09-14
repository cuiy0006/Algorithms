class Solution {
public:
    int maxArea(vector<int>& height) {
        int res = 0;
        int i = 0;
        int j = height.size() - 1;
        while(i < j){
            res = max(res, min(height[i], height[j]) * (j - i));
            if(height[j] > height[i]){
                ++i;
            } else {
                --j;
            }
        }
        return res;
    }
};
