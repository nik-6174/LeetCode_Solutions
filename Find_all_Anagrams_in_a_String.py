# Title: 438. Find All Anagrams in a String
# Difficulty: Medium
# Problem: https://leetcode.com/problems/find-all-anagrams-in-a-string/description

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_counter = Counter(p)
        substring_counter = defaultdict(int)

        for i in range(len(p)):
            substring_counter[s[i]] += 1

        res = [] if substring_counter != p_counter else [0]
        for idx, char in enumerate(s):
            if idx < len(p):
                continue
            substring_counter[char] += 1
            substring_counter[s[idx - len(p)]] -= 1
            if substring_counter[s[idx - len(p)]] == 0: del substring_counter[s[idx - len(p)]]

            if substring_counter == p_counter: res.append(idx - len(p) + 1)
        
        return res
