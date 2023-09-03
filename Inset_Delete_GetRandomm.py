# Title: 380. Insert Delete GetRandom O(1)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
       
        if val in self.dict:
            idx = self.dict[val]
            last = self.arr[-1]
            self.arr[idx] = last
            self.dict[last] = idx
            self.arr.pop()
            del self.dict[val]
            return True
        return False


    def getRandom(self) -> int:
        return choice(self.arr)
