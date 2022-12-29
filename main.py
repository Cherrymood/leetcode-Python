import solution1480
import solution1
import solution9
import solution13
import solution14
import solution20
import solution58
import solution21
import solution125
import solution421
import Solution1523

if __name__ == '__main__':
    solution1480 = solution1480.Solution()
    answer = solution1480.runningSum([1, 2, 3, 4])
    print(answer)

    answer = solution1480.runningSum([1, 1, 1, 1, 1])
    print(answer)

    answer = solution1480.runningSum([3, 1, 2, 10, 1])
    print(answer)

    solution1 = solution1.Solution()
    answer = solution1.twoSum([2, 7, 11, 15], 9)
    print(answer)

    answer = solution1.twoSum([3, 2, 4], 6)
    print(answer)

    answer = solution1.twoSum([3, 3], 6)
    print(answer)

    solution9 = solution9.Solution()
    answer = solution9.isPalindrome(121)
    print(answer)

    answer = solution9.isPalindrome(-121)
    print(answer)

    answer = solution9.isPalindrome(10)
    print(answer)

    solution13 = solution13.Solution()
    answer = solution13.romanToInt("III")
    print(answer)

    answer = solution13.romanToInt("LVIII")
    print(answer)

    answer = solution13.romanToInt("MCMXCIV")
    print(answer)

    solution14 = solution14.Solution()
    answer = solution14.longestCommonPrefix(["flower", "flow", "flight"])
    print(answer)

    answer = solution14.longestCommonPrefix(["dog", "racecar", "car"])
    print(answer)

    answer = solution14.longestCommonPrefix(["dog"])
    print(answer)

    solution20 = solution20.Solution()
    answer = solution20.isValid("()")
    print(answer)

    answer = solution20.isValid("(]")
    print(answer)

    answer = solution20.isValid("()[]{}")
    print(answer)

    answer = solution20.isValid("(")
    print(answer)

    answer = solution20.isValid("]")
    print(answer)

    solution58 = solution58.Solution()
    answer = solution58.lengthOfLastWord("Hello World")
    print(answer)

    answer = solution58.lengthOfLastWord("   fly me   to   the moon  ")
    print(answer)

    answer = solution58.lengthOfLastWord("luffy is still joyboy")
    print(answer)

    solution21 = solution21.Solution()
    answer = solution21.mergeTwoLists([1, 2, 4], [1, 3, 4])
    print(answer)

    answer = solution21.mergeTwoLists([], [])
    print(answer)

    answer = solution21.mergeTwoLists([], [0])
    print(answer)

    solution125 = solution125.Solution()
    answer = solution125.isPalindrome("A man, a plan, a canal: Panama")
    print(answer)

    answer = solution125.isPalindrome("race a car")
    print(answer)

    answer = solution125.isPalindrome(" ")
    print(answer)

    solution421 = solution421.Solution()
    answer = solution421.fizzBuzz(3)
    print(answer)

    answer = solution421.fizzBuzz(5)
    print(answer)

    answer = solution421.fizzBuzz(15)
    print(answer)

    answer = solution421.fizzBuzz(22)
    print(answer)

    Solution1523 = Solution1523.Solution()
    answer = Solution1523.countOdds(3, 8)
    print(answer)

    answer = Solution1523.countOdds(5, 9)
    print(answer)

    answer = Solution1523.countOdds(0,15)
    print(answer)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
