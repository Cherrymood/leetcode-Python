class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        a: str = "".join(sorted(s))
        b: str = "".join(sorted(t))

        if a != b:
            return False

        return True
