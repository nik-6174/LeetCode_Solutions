// TItle: 2125. Number of Laser Beams in a Bank
// Difficulty: Medium
// Problem: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description

class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int prev=0, count=0;

        for(string row : bank){
            int ones=0;
            for(char bit : row){
                if (bit == '1'){
                    ones++;
                }
            }
            count += ones * prev;
            if (ones)
            {
                prev = ones;
            }
        }
        return count;
    }
};
