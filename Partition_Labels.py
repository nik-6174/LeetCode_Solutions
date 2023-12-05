# Title: 763. Partition Labels
# Difficulty: Medium
# Problem: https://leetcode.com/problems/partition-labels/description

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        visited, ans = set(s[0]), []
        map = {}

        for i, char in enumerate(s):
            if char in map:
                map[char][1] = i
            else:
                map[char] = [i, i]
        
        queue, end = deque(), -1

        while end < len(s) - 1:
            start = end + 1
            queue.append(s[start])
            while queue:
                char = queue.popleft()
                end = max(end, map[char][1])

                for i in range(map[char][0] + 1, map[char][1]):
                    if s[i] not in visited:
                        queue.append(s[i])
                        visited.add(s[i])
            ans.append(end - start + 1)
        
        return ans
