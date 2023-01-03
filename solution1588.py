class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:

        result = 0

        for len_sub in range(1, len(arr) + 1, 2):
            for index in range(len(arr)):
                if (index + len_sub) > len(arr):
                    break
                result += sum(arr[index:index + len_sub])
        return result
