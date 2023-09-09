# Title: 649. Dota2 Senate
# Diffficulty: Medium
# Problem: https://leetcode.com/problems/dota2-senate/description/

# Optimal Solution using deque
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        d_turn = collections.deque()
        r_turn = collections.deque()

        for idx, s in enumerate(senate):
            if s == 'D':
                d_turn.append(idx)
            else:
                r_turn.append(idx)
        
        while d_turn and r_turn:
            nextD = d_turn.popleft()
            nextR = r_turn.popleft()

            if nextD < nextR:
                d_turn.append(nextD + n)
            else:
                r_turn.append(nextR + n)
        
        return 'Radiant' if r_turn else 'Dire'
        
# using just lists
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        arr = [i for i in senate]
        i = 0
        while True:
            if i >= len(arr):
                i = 0
            if len(arr) < 2:
                return 'Dire' if arr[0] == 'D' else 'Radiant'
            if arr[i] == 'D':
                flag = True
                for j in range(1,len(arr)):
                    if arr[(i + j) % len(arr)] == 'R':
                        arr.pop((i + j) % len(arr))
                        flag = False
                        break
                if flag:
                    return 'Dire'
            else:
                flag = True
                for j in range(1,len(arr)):
                    if arr[(i + j) % len(arr)] == 'D':
                        arr.pop((i + j) % len(arr))
                        flag = False
                        break
                if flag:
                    return 'Radiant'
            i += 1
