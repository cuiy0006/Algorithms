class Solution {
public:
    string countAndSay(int n) {
        string res = "1";
        for(int i = 2; i <= n; ++i){
            string tmp = "";
            int j = 0;
            while(j < res.size()){
                int cnt = 1;
                while(j != res.size() - 1 && res[j] == res[j + 1]){
                    ++cnt;
                    ++j;
                }
                tmp += to_string(cnt) + res[j];
                ++j;
            }
            if(j == res.size() - 1){
                tmp += to_string(1) + res[res.size() - 1];
            }
            res = tmp;
        }
        return res;
    }
};
