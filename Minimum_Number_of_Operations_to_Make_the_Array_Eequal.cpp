// Title: 2870. Minimum Number of Operations to Make Array Empty
// Difficulty: Medium
// Problem: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description

class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_map<int, int> counter;
        for (int i=0; i<nums.size(); ++i)
        {
            if (counter.find(nums[i]) != counter.end()){
                counter[nums[i]]++;
            }
            else{
                counter[nums[i]] = 1;
            }
        }

        int min_count = 0;
        for (auto it: counter){
            int count = it.second;
            if (count == 1){
                return -1;
            }
            if (count == 2){
                min_count++;
            }
            else{
                min_count += count/3;
                if (count % 3 != 0){
                    min_count++;
                }
            }  
        }
        return min_count;
    }
};
