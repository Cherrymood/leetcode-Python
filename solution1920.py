class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:

        ans: list = []

        for index in range(len(nums)):
            ans.append(nums[nums[index]])

        return ans