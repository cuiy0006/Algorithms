class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), [](vector<int>& v1, vector<int>& v2){
            return v1[0] < v2[0] || v1[0] == v2[0] && v1[1] > v2[1];
        });
        
        vector<int> idxs;
        for(size_t i = 0; i < people.size(); ++i){
            idxs.push_back(i);
        }
        
        vector<vector<int>> res(people.size());
        
        for(auto& one : people){
            int idx = idxs[one[1]];
            idxs.erase(idxs.begin() + one[1]);
            res[idx] = one;
        }
        
        return res;
    }
};
