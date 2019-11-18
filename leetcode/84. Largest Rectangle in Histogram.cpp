class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(-1);
        vector<int> stack;
        int res = 0;
        for(int i = 0; i < heights.size(); ++i){
            int h = heights[i];

            while(stack.size() != 0 && h < heights[stack[stack.size() - 1]]){
                int curr_idx = stack[stack.size() - 1];
                stack.pop_back();
                int prev_idx = stack.size() == 0? -1 : stack[stack.size() - 1];
                res = max(res, (i - prev_idx - 1) * heights[curr_idx]);
            }
            stack.push_back(i);
        }
        return res;
    }
};
