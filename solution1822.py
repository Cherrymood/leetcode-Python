class Solution:
    def arraySign(self, nums: list[int]) -> int:

        count_negative = 0

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                count_negative += 1

        if count_negative % 2 == 0:
            return 1
        elif count_negative % 2 != 0:
            return -1



