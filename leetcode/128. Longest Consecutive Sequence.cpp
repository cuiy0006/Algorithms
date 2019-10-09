class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> m;
        for(auto& num: nums){
            m[num] = 1;
        }
        
        int res = 0;
        for(auto it = m.begin(); it != m.end(); ++it){
            int cnt = 1;
            int next = it->first + 1;
            while(true){
                auto next_it = m.find(next);
                if(next_it == m.end()){
                    break;
                }
                cnt += m[next];
                m.erase(next_it);
                ++next;
            }
            it->second = cnt;
            res = max(res, cnt);
        }
        return res;
    }
};
