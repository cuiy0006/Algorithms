class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> res;
        int dic[26];
        for(size_t i = 0; i < S.size(); ++i){
            dic[S[i] - 'a'] = i;
        }
        
        int m = 0;
        int n = 0;
        
        for(size_t i = 0; i < S.size(); ++i){
            n = max(n, dic[S[i] - 'a']);
            if(i >= n){
                res.push_back(n - m + 1);
                m = n = i + 1;
            }
        }
        
        return res;
    }
};
