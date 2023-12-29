// Title: 1335. Minimum Difficulty of a Job Schedule
// Difficulty: Hard
// Problem: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description

class Solution {
public:
    int minDifficulty(std::vector<int>& jobDifficulty, int d) {
        int n = jobDifficulty.size();
        if (n < d) {
            return -1;
        }

        std::vector<std::vector<int>> memo(n, std::vector<int>(d, -1)); // Memoization array

        return dfs(jobDifficulty, d, 0, memo);
    }

private:
    int dfs(const std::vector<int>& jobDifficulty, int days, int index, std::vector<std::vector<int>>& memo) {
        int n = jobDifficulty.size();
        if (index == n && days == 0) {
            return 0;
        }
        if (index == n || days == 0) {
            return INT_MAX;
        }
        if (memo[index][days - 1] != -1) {
            return memo[index][days - 1];
        }

        int maxDifficulty = 0;
        int minDifficulty = INT_MAX;
        for (int i = index; i < n; ++i) {
            maxDifficulty = std::max(maxDifficulty, jobDifficulty[i]);
            int remainingDays = dfs(jobDifficulty, days - 1, i + 1, memo);
            if (remainingDays != INT_MAX) {
                minDifficulty = std::min(minDifficulty, maxDifficulty + remainingDays);
            }
        }

        memo[index][days - 1] = minDifficulty;
        return minDifficulty;
    }
};
