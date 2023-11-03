# Title: 140. Word Break II
# Difficulty: Hard
# Problem: https://leetcode.com/problems/word-break-ii/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        graph = {}
        for i in range(len(wordDict)):
            graph[wordDict[i]] = i


        res = [[] for _ in range(len(s) + 1)]
        res[len(s)] = [[-1]]

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    if dp[i + len(w)]:
                        dp[i] = True
                        res[i] += [[graph[w]] + elem for elem in res[i + len(w)]]

        return [' '.join([wordDict[i] for i in indexes[:-1]]) for indexes in res[0]]
