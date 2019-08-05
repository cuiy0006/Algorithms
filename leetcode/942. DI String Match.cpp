#include <vector>
class Solution {
public:
    vector<int> diStringMatch(string S) {
        std::vector<int> v(S.size() + 1);
        int min_val = 0;
        int max_val = 0;
        v[0] = 0;
        for(int i = 0; i < S.size(); ++i){
            if(S[i] == 'I'){
                v[i+1] = ++max_val;
            } else {
                v[i+1] = --min_val;
            }
        }
        for(int i = 0; i < v.size(); ++i){
            v[i] -= min_val;
        }
        return v;
    }
};
