class Solution:
    def hammingWeight(self, n: int) -> int:

        onces: int = bin(n).count("1")
        return onces


