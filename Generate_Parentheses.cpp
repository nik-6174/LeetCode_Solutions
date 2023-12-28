// Title: 22. Generate Parentheses
// Difficulty: Medium
// Problem: https://leetcode.com/problems/generate-parentheses/description/

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<vector<string>> dp(n + 1);
        dp[0] = {""};
        
        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < i; ++j) {
                vector<string>& left_parens = dp[j];
                vector<string>& right_parens = dp[i - j - 1];
                for (const string& left : left_parens) {
                    for (const string& right : right_parens) {
                        dp[i].push_back("(" + left + ")" + right);
                    }
                }
            }
        }
        
        return dp[n];
    }
};
