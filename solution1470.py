class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:

        x = nums[0:n]
        y = nums[n+1:-1]

        answer = []

        for index in range(len(nums)):
            answer.append(nums[index])
