from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_cuisine = {}
        self.sl = defaultdict(SortedList)
        for f, c, r in zip(foods, cuisines, ratings): 
            self.food_cuisine[f] = (c, r)
            self.sl[c].add((-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c, r = self.food_cuisine[food]
        self.sl[c].remove((-r, food))
        self.food_cuisine[food] = c, newRating
        self.sl[c].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.sl[cuisine][0][1]



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)