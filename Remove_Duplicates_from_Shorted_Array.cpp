// Title: 80. Remove Duplicates from Sorted Array II
// Difficulty: Medium
// Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 1)
        {
            return 1;
        }
        int k = 2;
        for (int i=2; i<nums.size(); i++)
        {
            if (nums[i] != nums[k-2])
            {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
};
