class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:

        INVALID_DISTANCE = 4294967295
        nearest_distance = INVALID_DISTANCE
        nearest_point = 0
        counter = 0

        for index, point in enumerate(points):
            a, b = point
            if a != x and b != y:
                counter += 1
            elif a == x or b == y:
                distance = abs(b - y) + abs(a - x)
                if distance < nearest_distance:
                    nearest_point = index
                    nearest_distance = distance

        if len(points) == counter:
            return -1
        else:
            return nearest_point







