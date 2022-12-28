import solution1480
import solution1
import solution9
import solution13
import solution14
import solution20

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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
