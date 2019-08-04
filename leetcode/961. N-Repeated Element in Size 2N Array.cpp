#include <unordered_set>
class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
        std::unordered_set<int> s;
        for(auto i = A.begin(); i != A.end(); ++i){
            if(s.find(*i) != s.end()){
                return *i;
            }
            s.emplace(*i);
        }
        return -1;
    }
};
