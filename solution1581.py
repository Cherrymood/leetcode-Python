class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        nums: str = str(n)
        l_nums = []
        product_nums = 1

        for num in nums:
            l_nums.append(int(num))

        for num in l_nums:
            product_nums *= num

        sum_nums: int = sum(l_nums)

        return product_nums - sum_nums
