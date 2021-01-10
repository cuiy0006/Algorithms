class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if(points.size() == 0) {
            return 0;
        }
        
        sort(points.begin(), points.end(), [](vector<int>& p1, vector<int>& p2){
            return p1[0] < p2[0];
        });
        
        int cnt = 0;
        auto curr = points[0];
        for(size_t i = 1; i < points.size(); ++i){
            if(curr[1] < points[i][0]){
                cnt += 1;
                curr[0] = points[i][0];
                curr[1] = points[i][1];
            } else {
                curr[0] = points[i][0];
                curr[1] = min(curr[1], points[i][1]);
            }
        }
        
        return cnt + 1;
    }
};
