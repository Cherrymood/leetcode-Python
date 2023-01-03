class Solution:
    def moveZeroes(self, nums: list[int]) -> None:

        for index in range(len(nums)):
            if nums[index] == 0:
                nums.insert(len(nums), nums[index])
                nums.remove(nums[index])


