# Title: 2336. Smallest Number in Infinite Set
# Difficulty: Medium
# Problem: https://leetcode.com/problems/smallest-number-in-infinite-set/description/?envType=study-plan-v2&envId=leetcode-75

class SmallestInfiniteSet:

    def __init__(self):
        self.not_inSet = set()
        self.smallest = 1
        

    def popSmallest(self) -> int:
        self.not_inSet.add(self.smallest)
        # store the smallest
        smallest = self.smallest
        # initialize the new smallest
        self.smallest += 1
        while self.smallest in self.not_inSet:
            self.smallest += 1 # increase smallest till it is not a number in removed numbers
        return smallest

        

    def addBack(self, num: int) -> None:
        if num in self.not_inSet:
            self.not_inSet.remove(num)
        # update the smallest
        if num < self.smallest:
            self.smallest = num
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
