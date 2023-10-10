# Title: 211. Design Add and Search Words Data Structure
# Difficulty: Medium
# Problem: https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class WordDictionary:

    def __init__(self):
        self.node = {}
        

    def addWord(self, word: str) -> None:
        node = self.node
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = 1

    def search(self, word: str) -> bool:
        def _search(word, i, node) -> bool:
            for j in range(i, len(word)):
                c = word[j]
                if c not in node:
                    if c == '.':
                        for x, n in node.items():
                            if x != '$' and _search(word, j+1, n):
                                return True
                    return False
                else:
                    node = node[c]
            return '$' in node

        return _search(word, 0, self.node)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
