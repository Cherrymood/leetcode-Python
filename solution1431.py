class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

        candies_plus_extraCandies: list[int] = []

        result: list[bool] = [True] * len(candies)

        for candy in candies:
            candies_plus_extraCandies.append(candy + extraCandies)

        for index in range(len(candies_plus_extraCandies)):
            for index_1 in range(len(candies)):
                if candies_plus_extraCandies[index] < candies[index_1]:
                    result[index] = False
                    break

        return result

