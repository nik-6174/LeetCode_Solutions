# Title: 2353. Design a Food Rating System
# Difficulty: Medium
# Problem: https://leetcode.com/problems/design-a-food-rating-system/description

# Memeory Efficient
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings = ratings
        self.cuisines = cuisines

        # map the index to the food for finding the food instantly
        self.index = {}
        for idx, food in enumerate(foods):
            self.index[food] = idx

        self.cuisine_type = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.cuisine_type[cuisine].append([-rating, food])
        for cuisine in self.cuisine_type:
            self.cuisine_type[cuisine].sort()


    def changeRating(self, food: str, newRating: int) -> None:
        index = self.index[food]
        old_rating = self.ratings[index]
        self.ratings[index] = newRating # update the rating
        cuisine = self.cuisines[index]
        # find the index for the old rating
        pop_index = bisect.bisect_left(self.cuisine_type[cuisine], [-old_rating, food])
        self.cuisine_type[cuisine].pop(pop_index)
        # insert the food with new rating
        insert_index = bisect.bisect_left(self.cuisine_type[cuisine],[-newRating, food])
        self.cuisine_type[cuisine].insert(insert_index, [-newRating, food])


    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_type[cuisine][0][1]



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

# Runtime Efficient
from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.__food_to_cuisine = {}
        self.__food_to_rating = {}
        self.__cusine_to_rating_foods = collections.defaultdict(SortedList)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.__food_to_cuisine[food] = cuisine
            self.__food_to_rating[food] = rating
            self.__cusine_to_rating_foods[cuisine].add((-rating, food))

    def changeRating(self, food, newRating):
        old_rating = self.__food_to_rating[food]
        cuisine = self.__food_to_cuisine[food]
        self.__cusine_to_rating_foods[cuisine].remove((-old_rating, food))
        self.__food_to_rating[food] = newRating
        self.__cusine_to_rating_foods[cuisine].add((-newRating, food))

    def highestRated(self, cuisine):
        return self.__cusine_to_rating_foods[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
