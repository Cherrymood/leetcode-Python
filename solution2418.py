class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:

        names_height = {}
        for index in range(len(heights)):
            names_height[heights[index]] = names[index]

        sorted_names_heights = dict(sorted(names_height.items(), reverse=True))

        return sorted_names_heights.values()