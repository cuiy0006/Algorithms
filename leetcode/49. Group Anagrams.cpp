class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;
        for(auto& str : strs){
            string key = str;
            sort(key.begin(), key.end());
            m[key].push_back(std::move(str));
        }
        
        vector<vector<string>> res;
        for(auto iter = m.begin(); iter != m.end(); ++iter){
            res.push_back(std::move(iter->second));
        }
        return res;
    }
};
