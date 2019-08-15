class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }
        unordered_map<char, int> m;
        for(int i = 0; i < s.size(); ++i){
            auto iter = m.find(s[i]);
            if(iter != m.end()){
                ++m[s[i]];
            } else {
                m.emplace(s[i], 1);
            }
        }
        
        for(int i = 0; i < t.size(); ++i){
            auto iter = m.find(t[i]);
            if(iter == m.end()){
                return false;
            } else if(m[t[i]] == 0) {
                return false;
            } else {
                --m[t[i]];
            }
        }
        return true;
    }
};
