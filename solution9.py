class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse_str_x = str(x)[::-1]
        reverse_int_x = int(reverse_str_x)
        if reverse_int_x == x:
            return True

        return False
