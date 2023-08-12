# Title: 424. Longest Repeating Character Replacement
# Difficulty: Medium
# Problem: https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = 0
        max_count = 0
        char_count = [0] * 26

        for right in range(len(s)):
            char_count[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, char_count[ord(s[right]) - ord('A')])

            while (right - left + 1 - max_count) > k:
                char_count[ord(s[left]) - ord('A')] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
