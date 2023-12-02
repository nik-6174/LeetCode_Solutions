# Title: 677. Map Sum Pairs
# Difficulty: Medium
# Problem: https://leetcode.com/problems/map-sum-pairs/description/

class MapSum:

    def __init__(self):
        self.trie = {} # use a trie
        self.words = {} # to know when same key is updated with another value
        

    def insert(self, key: str, val: int) -> None:
        # updating the word value
        if key in self.words:
            node = self.trie
            for char in key:
                node = node[char]
                node["value"] += val - self.words[key]
            self.words[key] = val
            return
        
        # new word is added
        self.words[key] = val
        node = self.trie
        for char in key:
            if char not in node:
                node[char] = {"value": 0}
            node = node[char]
            node["value"] += val


    def sum(self, prefix: str) -> int:
        node = self.trie
        for char in prefix:
            if char not in node:
                return 0
            node = node[char]
        return node["value"]



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
