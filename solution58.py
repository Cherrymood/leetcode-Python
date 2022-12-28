class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        without_spaces: list = s.split()
        length = len(without_spaces[len(without_spaces)-1])
        return length

