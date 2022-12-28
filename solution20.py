class Solution:
    def isValid(self, s: str) -> bool:

        stack: list = []
        dict = {"}": "{", "]": "[", ")": "("}
        open_brackets: list = ["{", "[", "("]
        closed_brackets: list = ["}", "]", ")"]
        new_char: str = ""

        for item in s:
            if item in open_brackets:
                stack.append(item)
            elif item in closed_brackets:
                if len(stack) == 0:
                    return False
                new_char = stack.pop()
                if new_char == dict[item]:
                    continue
                else:
                    return False

        return len(stack) == 0
