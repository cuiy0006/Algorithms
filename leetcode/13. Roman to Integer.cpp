class Solution {
public:
    int romanToInt(string s) {
        int last = 0;
        int res = 0;
        for(auto c : s){
            int num;
            switch(c){
                case 'I':
                    num = 1;
                    break;
                case 'V':
                    num = 5;
                    break;
                case 'X':
                    num = 10;
                    break;
                case 'L':
                    num = 50;
                    break;
                case 'C':
                    num = 100;
                    break;
                case 'D':
                    num = 500;
                    break;
                default:
                    num = 1000;
            }
            res += num;
            if(num > last){
                res -= 2 * last;
            }
            last = num;
        }
        return res;
    }
};
