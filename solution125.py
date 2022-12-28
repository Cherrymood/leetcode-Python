class Solution:
    def isPalindrome(self, s: str) -> bool:
        low_case = s.lower()
        without_space = "".join(low_case.split())

        palindrome = ""

        for item in without_space:
            if item.isalnum():
                palindrome += item
            else:
                continue

        if palindrome == palindrome[::-1]:
            return True
        else:
            return False
