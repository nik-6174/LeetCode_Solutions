# Title: 605. Can Place Flowers
# Difficulty: Easy
# Problem: https://leetcode.com/problems/can-place-flowers/description/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True

        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            else:
                return False
        
        if len(flowerbed) > 1 and (not flowerbed[0]) and (not flowerbed[1]):
            flowerbed[0] = 1
            n -= 1
            if not n:
                return True
        
        for i in range(1, len(flowerbed)-1):
            if (not flowerbed[i]) and (not flowerbed[i-1]) and (not flowerbed[i+1]):
                flowerbed[i] = 1
                n -= 1
                if not n:
                    return True
        
        if len(flowerbed) > 1 and (not flowerbed[-1]) and (not flowerbed[-2]):
            n -= 1
            if not n:
                return True
        return False if n > 0 else True
