class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        unordered_map<char, int> m;
        int max_len = 0;
        int i = 0;
        
        for(int j = 0; j < s.size(); ++j){
            if(m.find(s[j]) != m.end()){
                m[s[j]] += 1;
                max_len = max(max_len, j - i + 1);
            } else {
                m[s[j]] = 1;
                if(m.size() <= k){
                    max_len = max(max_len, j - i + 1);
                } else {
                    while(m.size() > k){
                        --m[s[i]];
                        if(m[s[i]] == 0){
                            m.erase(s[i]);
                        }
                        ++i;
                    }
                }
            }
        }
        
        return max_len;
    }
};
