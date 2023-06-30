# Title: Word Break (LeetCode)
# Difficulty : Medium
# Problem : https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = []
        for i in range(len(s)):
            if s[:i+1] in wordDict: # if the entire substring is a word in the wordDict
                dp.append(True)
            else:
                # set flag to check if the substring can be formed using the words in wordDict
                flag = True
                j = i-1
                while j >= 0:
                    # check if any combination of previously formed substrings and a word in the dictionary can form the current substring
                    if dp[j] and s[j+1:i+1] in wordDict:
                        dp.append(True)
                        # set flag to False so we don't append False
                        flag=False
                        break
                    j -= 1
                # conclude that the substring could not be formed using the words in wordDict
                if flag:
                    dp.append(False)
        # return if the whole string can be formed with the words in the dictionary
        return dp[-1]
