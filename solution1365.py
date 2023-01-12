class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:

        nums1 = sorted(nums)
        dic = {}
        answer = []

        for index, value in enumerate(nums1):
            dic.setdefault(value, index)

        for i in range(0, len(nums)):
            answer.append(dic[nums[i]])

        return answer



