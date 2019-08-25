class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> res;
        if(numRows == 0){
            return res;
        }
        vector<int> first = {1};
        res.push_back(first);
        for(int i = 1; i < numRows; ++i){
            vector<int> row;
            vector<int>& last_row = res[res.size() - 1];
            row.push_back(last_row[0]);
            for(int j = 1; j <= i - 1; ++j){
                row.push_back(last_row[j - 1] + last_row[j]);
            }
            row.push_back(last_row[last_row.size() - 1]);
            res.push_back(row);
        }
        return res;
    }
};
