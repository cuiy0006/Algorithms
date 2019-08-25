class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> dic;
        for(int i = 0; i < nums.size(); ++i){
            if(dic.find(nums[i]) == dic.end()){
                dic.emplace(nums[i], i);
            }
        }
        
        vector<int> res;
        for(int i = 0; i < nums.size(); ++i){
            int other = target - nums[i];
            auto it = dic.find(other);
            if(it != dic.end() && i != dic[other]){
                res.push_back(i);
                res.push_back(dic[other]);
                return res;
            }
        }
        return res;
    }
};
