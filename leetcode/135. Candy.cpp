class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> v(ratings.size(), 1);
        
        int i = 1;
        int j = ratings.size() - 2;
    
        while(i < ratings.size()) {
            if(ratings[i] > ratings[i - 1]){
                v[i] = v[i - 1] + 1;
            }
            ++i;
        }
        
        while(j >= 0) {
            if(ratings[j] > ratings[j + 1]){
                v[j] = max(v[j], v[j + 1] + 1);
            }
            --j;
        }
        
        int res = 0;
        for(auto c: v){
            res += c;
        }
        
        return res;
    }
};
