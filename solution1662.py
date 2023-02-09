class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        word: str = "".join(word1)
        word3: str = "".join(word2)

        if word == word3:
            return True

        return False