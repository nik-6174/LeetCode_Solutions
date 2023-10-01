# Title: 1268. Search Suggestions System
# Difficulty: Medium
# Problem: https://leetcode.com/problems/search-suggestions-system/description/


## Using Two Pointers
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #two pointers
        res = []
        products.sort() #lexi order
        left, right = 0, len(products)-1

        for i in range(len(searchWord)):
            ch = searchWord[i]
            #shrink the range if not match
            while left<=right and (len(products[left])<=i or products[left][i]!=ch):
                left += 1
            while left<=right and (len(products[left])<=i or products[right][i]!=ch):
                right -=1 
            #valid words range
            valid = right-left+1
            words = [] #list of valid words
            for j in range(min(3, valid)):
                words.append(products[left+j])
            res.append(words)
        return res


## Using Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        products.sort()
        
        # Insert products into the trie
        for product in products:
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                if len(node.suggestions) < 3:
                    node.suggestions.append(product)
        
        result = []
        node = root
        found = True
        
        # Traverse the trie while typing characters
        for char in searchWord:
            if char in node.children and found:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                found = False
                result.append([])
        
        # Ensure the result has the correct length
        while len(result) < len(searchWord):
            result.append([])
        
        return result
