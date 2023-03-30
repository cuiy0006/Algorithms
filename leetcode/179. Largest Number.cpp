class Solution {
public:
    string largestNumber(vector<int>& nums) {
        std::sort(nums.begin(), nums.end(), [](int a, int b){
            std::string as = std::to_string(a);
            std::string bs = std::to_string(b);
            return as + bs > bs + as;
        });

        if (nums[0] == 0) {
            return "0";
        }

        std::string res;
        for (auto num : nums) {
            res.append(std::to_string(num));
        }
        return res;
    }
};
