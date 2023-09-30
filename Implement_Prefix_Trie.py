# Title: 208. Implement Trie (Prefix Tree)
# Difficulty: Medium
# Problem: https://leetcode.com/problems/implement-trie-prefix-tree/description/

class Trie:

    def __init__(self):
        self.trie = {}


    def insert(self, word: str) -> None:
        pointer = self.trie
        for char in word:
            if char not in pointer:
                pointer[char] = {}
            pointer = pointer[char]
        pointer["*"] = None
        

    def search(self, word: str) -> bool:
        pointer = self.trie
        for char in word:
            if char not in pointer:
                return False
            pointer = pointer[char]
        return "*" in pointer
        

    def startsWith(self, prefix: str) -> bool:
        pointer = self.trie
        for char in prefix:
            if char not in pointer:
                return False
            pointer = pointer[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
