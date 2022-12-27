class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        strs.sort()
        longest_prefix = ""

        for index in range(len(strs[0])):
            if strs[0][index] == strs[len(strs) - 1][index]:
                longest_prefix += strs[0][index]
            else:
                break

        return longest_prefix
