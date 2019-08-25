class Solution {
public:
    bool isHappy(int n) {
        set<int> s;
        while(true){
            int tmp = 0;
            while(n != 0){
                tmp += pow(n % 10, 2);
                n = n / 10;
            }
            if(tmp == 1){
                return true;
            } else if(s.find(tmp) != s.end()){
                return false;
            } else {
                s.emplace(tmp);
            }
            n = tmp;
        }
        return false;
    }
};
