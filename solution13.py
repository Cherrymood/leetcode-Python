class Solution:
    def romanToInt(self, s: str) -> int:

        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        new_nums = 0
        p = len(s)

        for index in range(len(s)-1, -1, -1):
            if index+1 != len(s) and dict[s[index+1]] > dict[s[index]]:
                new_nums -= dict[s[index]]
            else:
                new_nums += dict[s[index]]

        return new_nums

