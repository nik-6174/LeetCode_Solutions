// Title: 907. Sum of Subarray Minimums
// Difficulty: Medium
// Problem: https://leetcode.com/problems/sum-of-subarray-minimums/description/

class Solution {
public:
    int sumSubarrayMins(vector<int>& arr) {
        arr.push_back(-1);
        int res = 0, MOD =1e9+7;
        vector<int> stack;

        for(int i=0; i<arr.size(); i++){
            while (!stack.empty()){
                int mid = stack.back();
                if (arr[mid] >= arr[i]){
                    stack.pop_back();
                    int pivot = mid;
                    int min_val = arr[mid];
                    int right = i - pivot;
                    int left = pivot;
                    if (!stack.empty()){
                        int back = stack.back();
                        left -= back;
                    }
                    else{
                        left++;
                    }
                    long int combinations = (left * right) % MOD;
                    res += (combinations * min_val) % MOD;
                    res = res % MOD;
                }
                else{
                    break;
                }
            }
            stack.push_back(i);
        }
        return res;
    }
};
