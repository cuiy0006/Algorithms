class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> s;
        for(auto num: nums){
            auto iter = s.find(num);
            if(iter != s.end()){
                return true;
            }
            s.emplace(num);
        }
        return false;
    }
};
