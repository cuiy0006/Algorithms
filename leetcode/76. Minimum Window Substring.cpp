class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> m;
        for(char c : t){
            if(m.find(c) == m.end()){
                m[c] = 1;
            } else {
                m[c] += 1;
            }

        }
        
        
        int cnt = t.size();
        int minlen = s.size() + 1;
        int start = 0;
        int end = -1;
        int i = 0;
        int j = 0;

        while(j < s.size()){
            if(m.find(s[j]) != m.end()){
                --m[s[j]];
                if(m[s[j]] >= 0){
                    cnt -= 1;
                }
                
                while(cnt == 0){
                    if(j - i + 1 < minlen){
                        start = i;
                        end = j;
                        minlen = j - i + 1;
                    }
                    if(m.find(s[i]) != m.end()){
                        ++m[s[i]];
                        if(m[s[i]] > 0){
                            ++cnt;
                            ++i;
                            break;
                        }
                    }
                    ++i;
                }
            }
            ++j;
        }
        
        string res = "";
        for(int k = start; k <= end; ++k){
            res += s[k];
        }
        return res;
    }
};
