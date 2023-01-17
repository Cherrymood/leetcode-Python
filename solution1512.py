class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:

        answer: int = 0

        if len(nums) == 1:
            return answer

        for index_1 in range(len(nums)):
            for index_2 in range(index_1+1, len(nums)):
                if nums[index_1] == nums[index_2]:
                    answer += 1

        return answer


