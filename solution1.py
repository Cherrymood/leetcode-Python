class Solution:
    def twoSum(self, nums: list[int], target: int) -> object:
        for index in range(len(nums)):
            for index_1 in range(index + 1, len(nums)):
                if (nums[index] + nums[index_1]) == target:
                    return [index, index_1]
                else:
                    continue
