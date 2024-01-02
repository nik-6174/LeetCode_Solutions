// 2610. Convert an Array Into a 2D Array With Conditions
// Difficulty: Medium
// Problem: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description

class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        vector<vector<int>> ans;
        map <int, int> counter;

        for (int num : nums)
        {
            if (counter.find(num) == counter.end()){
                counter[num] = 1;
            }
            else{
                counter[num]++;
            }

            if (ans.size() < counter[num])
            {
                ans.push_back({num});
            }
            else{
                ans[counter[num]-1].push_back(num);
            }
        }
        return ans;
    }
};
