class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxsum = nums[0]
        subsum = 0

        for num in nums:
            if subsum < 0:
                subsum = 0
            subsum += num
            maxsum = max(maxsum, subsum)

        return maxsum

import solution53

if __name__ == '__main__':

    solution53 = solution53.Solution()
    answer = solution53.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(answer)