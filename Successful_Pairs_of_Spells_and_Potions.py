class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()

        for spell_strength in spells:
            portion_min = math.ceil(success / spell_strength)
            count = len(potions) - self.binary_search(potions, portion_min)
            res.append(count)

        return res

    def binary_search(self, potions, target):
        left, right = 0, len(potions) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if potions[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
