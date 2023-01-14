class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        result = [""] * len(s)

        for index_letter in range(len(s)):
            result[indices[index_letter]] = s[index_letter]

        return "".join(result)
