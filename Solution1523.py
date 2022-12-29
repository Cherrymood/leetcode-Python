class Solution:
    def countOdds(self, low: int, high: int) -> int:

        length: int = len(range(low, high+1))

        if low % 2 != 0 and high % 2 != 0:
            return int((length+1) / 2)
        elif low % 2 == 0 or high % 2 == 0:
            return int(length / 2)

