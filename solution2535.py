class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:

        sum_nums: int = sum(nums)
        digit_sum_nums: int = 0

        for num in nums:
            if num < 10:
                digit_sum_nums += num
            elif num < 100:
                a = num % 10
                digit_sum_nums += a
                num = num // 10
                digit_sum_nums += num
            elif num <= 2000:
                a = num % 10
                digit_sum_nums += a
                num = num // 10
                a = num % 10
                digit_sum_nums += a
                num = num // 10
                a = num % 10
                digit_sum_nums += a
                num = num // 10
                digit_sum_nums += num

        return abs(sum_nums - digit_sum_nums)


