class Solution:
    def maximumCount(self, nums: list[int]) -> int:

        pos: int = 0
        neg: int = 0

        for num in nums:
            if num == 0:
                continue
            elif num > 0:
                pos += 1
            else:
                neg += 1

        if pos > neg:
            return pos
        else:
            return neg