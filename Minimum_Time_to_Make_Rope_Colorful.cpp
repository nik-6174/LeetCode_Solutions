// Title: 1578. Minimum Time to Make Rope Colorful
// Difficulty: Medium
// Problem: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description

class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int total_sum = accumulate(neededTime.begin(), neededTime.end(), 0);

        char prev = colors[0];
        int max_time = neededTime[0];

        char end = 'X';
        colors.push_back(end);
        neededTime.push_back(0);

        for (int i=0; i<neededTime.size(); i++)
        {
            if (colors[i] == prev)
            {
                max_time = max(max_time, neededTime[i]);
            }
            else
            {
                total_sum -= max_time;
                max_time = neededTime[i];
                prev = colors[i];
            }
        }
        return total_sum;
    }
};
