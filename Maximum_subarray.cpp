// Title: 53. Maximum Subarray
// Difficulty: Medium
// Problem: https://leetcode.com/problems/maximum-subarray/description/

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        long long int cumsum = 0;
        int max_sum = nums[0];

        for (int i=0; i<nums.size(); i++)
        {
            cumsum += nums[i];
            if (cumsum > max_sum)
            {
                max_sum = cumsum;
            }
            if (cumsum < 0)
            {
                cumsum = 0;
            }
        }
        return max_sum;
    }
};
