class Solution:
    def reverseWords(self, s: str) -> str:

        b = s.split()
        result = ""

        for index in range(len(b)):
            if index != (len(b) - 1):
                result += b[index][::-1] + " "
            else:
                result += b[index][::-1]

        return result