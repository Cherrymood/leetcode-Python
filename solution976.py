class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:

        if len(nums) <= 2:
            return 0

        nums.sort(reverse = True)

        for index in range(len(nums)-2):

            if nums[index] < (nums[index+1] + nums[index+2]):
                return nums[index] + nums[index+1] + nums[index+2]

        return 0

