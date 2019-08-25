class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        unordered_map<int, int> map;
        for(auto num: nums1){
            auto it = map.find(num);
            if(it == map.end()){
                map.emplace(num, 1);
            } else {
                map[num]++;
            }
        }
        
        for(auto num: nums2){
            auto it = map.find(num);
            if(it != map.end() && map[num] != 0){
                res.push_back(num);
                map[num]--;
            }
        }
        return res;
    }
};
