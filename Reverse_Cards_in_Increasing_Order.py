# Title: 950. Reveal Cards In Increasing Order
# Difficulty: Medium
# Problem: https://leetcode.com/problems/reveal-cards-in-increasing-order/description/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # sort the deck first
        deck.sort()

        # find the positions of sorted element in the output
        indexes = deque(range(len(deck)))
        res = [0]*len(deck) # initialize the new deck to sorted the cards
        i = 0
        while indexes:
            # fill the ith sorted number at the popped index
            res[indexes.popleft()] = deck[i]
            if indexes: # keep the next card at the bottom
                indexes.append(indexes.popleft())
            i += 1
        return res
