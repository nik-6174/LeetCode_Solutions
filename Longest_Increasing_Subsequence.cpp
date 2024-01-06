// Title: 300. Longest Increasing Subsequence
// Difficulty: Medium
// Problem: https://leetcode.com/problems/longest-increasing-subsequence/description/

// Using Dynamic Programming: O(n^2)
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);
        int max_len = 1;

        for (int i=1; i<nums.size(); i++){
            for (int j=0; j<i; j++){
                if (nums[j] < nums[i]){
                    dp[i] = max(dp[i], dp[j]+1);
                }
            }
            max_len = max(max_len, dp[i]);
        }
        return max_len;
    }
};

// Using Vectors and binary Search: O(n logn)
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
 
        vector<int> sub;

        for(int x : nums) {
            if(sub.empty() || sub[sub.size()-1] < x) {
                sub.push_back(x);
            }
            else {
                auto idx = lower_bound(sub.begin(), sub.end(), x);
                *idx = x;
            }
        }

        return sub.size();
    }
};
