class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        runningSum = []

        for index in range(len(nums)):
            if index == 0:
                runningSum.append(nums[index])
            else:
                runningSum.append(runningSum[index-1] + nums[index])

        return runningSum