class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int>& v1, vector<int>& v2){
            return v1[1] < v2[1];
        });
        
        int cnt = 0;
        int i = 0;
        int j = 1;
        while(j < intervals.size()) {
            if(intervals[i][1] <= intervals[j][0]){
                i = j;
            } else {
                cnt += 1;
            }
            ++j;
        }
        
        return cnt;
    }
};
