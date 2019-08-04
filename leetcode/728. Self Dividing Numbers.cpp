#include <vector>
class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        std::vector<int> res;
        for(int i = left; i <= right; ++i){
            int val = i;
            if(val == 0){
                continue;
            }
            while(val != 0){
                int digit = val % 10;
                if(digit == 0){
                    break;
                }
                if(i % digit != 0){
                    break;
                }
                val = val / 10;
            }
            if(val == 0){
                res.push_back(i);
            }
        }
        return res;
    }
};
