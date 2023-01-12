class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:

        result = 0

        for item in operations:
            if item == "++X" or item == "X++":
                result += 1
            elif item == "--X" or item == "X--":
                result -= 1

        return result

