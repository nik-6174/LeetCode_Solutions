// Title: 5. Longest Palindromic Substring
// Difficulty: Medium
// Problem: https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution {
public:
    string longestPalindrome(string s) {
        string extended = "^";
        for (char c : s) {
            extended += "#";
            extended += c;
        }
        extended += "#$";

        int n = extended.size();
        vector<int> p(n, 0);
        int center = 0, right = 0;

        for (int i = 1; i < n - 1; ++i) {
            int j = 2 * center - i;

            if (right > i) {
                p[i] = min(right - i, p[j]);
            }

            while (extended[i + 1 + p[i]] == extended[i - 1 - p[i]]) {
                p[i]++;
            }

            if (i + p[i] > right) {
                center = i;
                right = i + p[i];
            }
        }

        int max_len = 0, center_index = 0;
        for (int i = 1; i < n - 1; ++i) {
            if (p[i] > max_len) {
                max_len = p[i];
                center_index = i;
            }
        }

        int start_index = (center_index - max_len) / 2;
        return s.substr(start_index, max_len);
    }
};
