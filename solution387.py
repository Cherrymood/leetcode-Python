class Solution:
    def firstUniqChar(self, s: str) -> int:

        counter: int = 0

        for index in range(len(s)):
            counter += s.count(s[index])
            if counter == 1:
                return index
            else:
                counter = 0

        return -1