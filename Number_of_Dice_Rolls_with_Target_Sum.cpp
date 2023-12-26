// Title: 1155. Number of Dice Rolls With Target Sum
// Difficulty: Medium
// Problem: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description

class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        int dp[30][1001] = {0};
        int i, j;
        int mod = 1e9 + 7;
        for (j = 1; j <= k && j <= target; j++) {
            dp[0][j] = 1;
        }
        for (i = 1; i < n; i++) {
            for (j = 1; j <= target; j++) {
                dp[i][j] = (dp[i - 1][j - 1] + dp[i][j - 1]) % mod;
                if (j > k) {
                    dp[i][j] = (dp[i][j] - dp[i - 1][j - 1 - k] + mod) % mod;
                }
            }
        }
        return dp[n - 1][target];
    }
};
