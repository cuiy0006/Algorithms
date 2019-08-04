
#include <unordered_set>

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        std::unordered_set<char> s(J.begin(), J.end());
        int cnt = 0;
        for(size_t i = 0; i < S.size(); ++i){
            if(s.find(S[i]) != s.end()){
                ++cnt;
            }
        }
        return cnt;
    }
};
