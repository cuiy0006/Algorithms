class Solution {
public:
    bool judgeSquareSum(int c) {
        for(int a = 0; a < int(sqrt(c)) + 1; ++a){
            double b = sqrt(c - pow(a, 2));
            if(b == int(b)){
                return true;
            }
            if(b <= a){
                return false;
            }
        }
        return false;
    }
};
