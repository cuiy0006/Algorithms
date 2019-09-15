class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> v;
        int m = 1;
        int i = 1;
        v.push_back(0);
        while(i <= num){
            int j = 0;
            while(i < m && i <= num){
                v.push_back(v[j] + 1);
                ++i;
                ++j;
            }
            m = m * 2;
        }
        return v;
    }
};
