# Title: 212. Word Search II
# Difficulty: Hard
# Problem: https://leetcode.com/problems/word-search-ii/description/

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create a Trie
        self.trie = {}
        for word in words:
            pointer = self.trie
            for letter in word:
                if letter not in pointer:
                    pointer[letter] = {}
                pointer = pointer[letter]
            pointer['$'] = word

        n, m, res = len(board), len(board[0]), set()

        # Define a depth-first search to search for letters in a word
        def dfs(i, j, pointer):
            if '$' in pointer:
                res.add(pointer["$"])

            original_char = board[i][j]
            board[i][j] = '#'  # Mark the cell as visited
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and board[x][y] in pointer:
                    dfs(x, y, pointer[board[x][y]])

            board[i][j] = original_char  # Restore the original character

        # Start searching for words starting with each letter in the board
        for i in range(n):
            for j in range(m):
                if board[i][j] in self.trie:
                    dfs(i, j, self.trie[board[i][j]])

        return list(res)  # Return all unique answers
