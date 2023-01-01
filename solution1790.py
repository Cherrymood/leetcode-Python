class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1_check = ""
        s2_check = ""

        for index in range(len(s1)):
            if s1[index] != s2[index]:
                if len(s1_check) > 2:
                    return False
                else:
                    s1_check += s1[index]
                    s2_check += s2[index]
            elif s1[index] == s2[index]:
                continue

        if s1_check == s2_check:
            return True
        else:
            return False

        return True
