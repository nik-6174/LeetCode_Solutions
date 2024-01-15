# Title: 2225. Find Players With Zero or One Losses
# Difficulty: Medium
# Problem: https://leetcode.com/problems/find-players-with-zero-or-one-losses/description

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        lost_once = set()
        lost_more = set()

        for match in matches:
            if match[1] in lost_once:
                lost_more.add(match[1])
                lost_once.remove(match[1])
            elif match[1] not in lost_more:
                lost_once.add(match[1])
            players.add(match[0])
            players.add(match[1])
        
        return [sorted(list(players - lost_once - lost_more)), sorted(list(lost_once))]
