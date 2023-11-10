# TItle: 76. Minimum Window Substring
# Difficulty: Hard
# Problem: https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # handling edge cases
        if len(t) > len(s):
            return ""
        if not set(t).issubset(set(s)):
            return ""
        if t == s:
            return t
        
        counterT = Counter(t)
        extra = {} # store the extra elements
        min_length, ans = float('inf'), ""
        start, end = 0, 0

        # find the minimum window that has t as substring
        for idx, char in enumerate(s):
            if char in counterT and counterT[char] > 0:
                counterT[char] -= 1
                if counterT[char] == 0:
                    del counterT[char]
            else:
                if char not in extra:
                    extra[char] = 1
                else:
                    extra[char] += 1
            
            # we have the required window with t as the substring
            if not counterT:
                # remove extra characters from the start of the window
                while start < len(s) and s[start] in extra and extra[s[start]] > 0:
                    extra[s[start]] -= 1
                    start += 1

                # update the minimum length
                if min_length > idx - start + 1:
                    min_length = idx - start + 1
                    ans = s[start:idx+1]
                end = idx + 1
                break # break as the loop as it's fullfilled its purpose

        # find the length of all possible windows ending at idx in s
        for idx in range(end, len(s)):
            # add new character to the end of the window
            if s[idx] not in extra:
                extra[s[idx]] = 1
            else:
                extra[s[idx]] += 1

            # remove the extra characters from the start of the window
            while start < len(s) and s[start] in extra and extra[s[start]] > 0:
                extra[s[start]] -= 1
                start += 1
            # update the minimum length
            if min_length > idx - start + 1:
                min_length = idx - start + 1
                ans = s[start:idx+1]

        return ans
