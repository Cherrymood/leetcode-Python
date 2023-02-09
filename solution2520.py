class Solution:
    def countDigits(self, num: int) -> int:

        counter = 0
        num1 = num

        while num != 0:
            val = num % 10
            if num1 % val == 0:
                counter += 1
            num = num // 10

        return counter