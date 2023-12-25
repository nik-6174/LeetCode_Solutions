// Title: 91. Decode Ways
// Difficulty: Medium
// Problem: https://leetcode.com/problems/decode-ways/description

class Solution {
public:
    int numDecodings(string s) {
        if (s[0] == '0') {
            return 0;
        }

        int n = s.length();
        std::vector<int> dp(n + 1, 0);

        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i <= n; i++) {
            if (s[i - 1] != '0') {
                dp[i] = dp[i - 1];
            }

            int twoDigit = std::stoi(s.substr(i - 2, 2));
            if (twoDigit >= 10 && twoDigit <= 26) {
                dp[i] += dp[i - 2];
            }
        }

        return dp[n];
    }
};
