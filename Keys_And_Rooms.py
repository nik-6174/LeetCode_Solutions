# Title: 841. Keys and Rooms
# Difficulty: Medium
# Problem: https://leetcode.com/problems/keys-and-rooms/description/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        arr = [0]
        while arr:
            n = len(arr)
            for _ in range(n):
                if arr[0] not in visited:
                    visited.add(arr[0])
                    arr += rooms[arr[0]]
                arr.pop(0)
        return visited == set(range(len(rooms)))
