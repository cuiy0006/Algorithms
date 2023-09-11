class Solution {
public:
    int numWays(int n, int k) {
        if (n == 1) {
            return k;
        }
        vector<int> dp(n);
        dp[0] = k;
        dp[1] = k * k;
        for (size_t i = 2; i < n; i++) {
            dp[i] = dp[i - 2] * (k - 1) + dp[i - 1] * (k - 1);
        }
        return dp[n - 1];
    }
};




class Solution {
public:
    int numWays(int n, int k) {
        unordered_map<int, int> dp;
        return totalWays(n, k, dp);
    }
    
private:
    int totalWays(int i, int k, unordered_map<int, int>& dp) {
        if (i == 1) {
            return k;
        } else if (i == 2) {
            return k * k;
        }
        
        if (dp.find(i) == dp.end()) {
            dp[i] = (k-1) * totalWays(i-1, k, dp) + (k-1) * totalWays(i-2, k, dp);
        }
        
        return dp[i];
    }
};
