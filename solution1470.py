class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:

        x = nums[0:n]
        y = nums[n:(len(nums))]

        answer = []

        for index in range(len(x)):
            answer.append(x[index])
            answer.append(y[index])

        return answer
