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
import solution1491
import solution1581
import solution191
import solution66
import solution231
import solution976
import solution1790
import solution1502
import solution1822
import solution202
import solution496
import solution1588
import solution1672
import solution283
import solution1779


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

    solution1491 = solution1491.Solution()
    answer = solution1491.average([4000,3000,1000,2000])
    print(answer)

    answer = solution1491.average([4000,4700,7000])
    print(answer)

    solution1581 = solution1581.Solution()
    answer = solution1581.subtractProductAndSum(234)
    print(answer)

    answer = solution1581.subtractProductAndSum(4421)
    print(answer)

    answer = solution1581.subtractProductAndSum(5555)
    print(answer)

    solution191 = solution191.Solution()
    answer = solution191.hammingWeight(1011)
    print(answer)

    answer = solution191.hammingWeight(10000000)
    print(answer)

    answer = solution191.hammingWeight(11111111111111111111111111111101)
    print(answer)

    solution66 = solution66.Solution()
    answer = solution66.plusOne([1,2,3])
    print(answer)

    answer = solution66.plusOne([4,3,2,2])
    print(answer)

    answer = solution66.plusOne([9])

    answer = solution66.plusOne([9, 9, 9, 9])
    print(answer)

    solution231 = solution231.Solution()
    answer = solution231.isPowerOfTwo(1)
    print(answer)

    answer = solution231.isPowerOfTwo(16)
    print(answer)

    answer = solution231.isPowerOfTwo(3)
    print(answer)

    answer = solution231.isPowerOfTwo(-15)
    print(answer)

    solution976 = solution976.Solution()
    answer = solution976.largestPerimeter([2, 1, 2])
    print(answer)

    answer = solution976.largestPerimeter([1,2,1,10])
    print(answer)

    answer = solution976.largestPerimeter([3,6,2,3])
    print(answer)

    solution1790 = solution1790.Solution()
    answer = solution1790.areAlmostEqual("bank", "kanb")
    print(answer)

    answer = solution1790.areAlmostEqual("attack", "defend")
    print(answer)

    answer = solution1790.areAlmostEqual("kelb", "kelb")
    print(answer)

    answer = solution1790.areAlmostEqual("aa", "ac")
    print(answer)

    answer = solution1790.areAlmostEqual("aab", "acb")
    print(answer)

    answer = solution1790.areAlmostEqual("ca", "ac")
    print(answer)

    solution1502 = solution1502.Solution()
    answer = solution1502.canMakeArithmeticProgression([3, 5, 1])
    print(answer)

    answer = solution1502.canMakeArithmeticProgression([1, 2, 4])
    print(answer)

    answer = solution1502.canMakeArithmeticProgression([13, 12, -12, 9, 9, 16, 7, -10, -20, 0, 18, -1, -20, -10, -8, 15, 15, 16, 2, 15])
    print(answer)

    solution1822 = solution1822.Solution()
    answer = solution1822.arraySign([-1, -2, -3, -4, 3, 2, 1])
    print(answer)

    answer = solution1822.arraySign([1, 5, 0, 2, -3])
    print(answer)

    answer = solution1822.arraySign([-1, 1, -1, 1, -1])
    print(answer)

    solution202 = solution202.Solution()
    answer = solution202.isHappy(19)
    print(answer)

    answer = solution202.isHappy(2)
    print(answer)

    answer = solution202.isHappy(4)
    print(answer)

    solution496 = solution496.Solution()
    answer = solution496.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
    print(answer)

    answer = solution496.nextGreaterElement([2, 4], [1, 2, 3, 4])
    print(answer)

    solution1588 = solution1588.Solution()
    answer = solution1588.sumOddLengthSubarrays([1,4,2,5,3])
    print(answer)

    answer = solution1588.sumOddLengthSubarrays([1, 2])
    print(answer)

    answer = solution1588.sumOddLengthSubarrays([10,11,12])
    print(answer)

    solution1672 = solution1672.Solution()
    answer = solution1672.maximumWealth([[1,2,3],[3,2,1]])
    print(answer)

    answer = solution1672.maximumWealth([[1,5],[7,3],[3,5]])
    print(answer)

    answer = solution1672.maximumWealth([[2,8,7],[7,1,3],[1,9,5]])
    print(answer)

    solution283 = solution283.Solution()
    answer = solution283.moveZeroes([0,1,0,3,12])
    print(answer)

    answer = solution283.moveZeroes([0])
    print(answer)

    solution1779 = solution1779.Solution()
    answer = solution1779.nearestValidPoint(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]])
    print(answer)

    answer = solution1779.nearestValidPoint(3, 4, [[3, 4]])
    print(answer)

    answer = solution1779.nearestValidPoint(3, 4, [[2, 3]])
    print(answer)

    answer = solution1779.nearestValidPoint(1, 1, [[1, 2], [3, 3], [3, 3]])
    print(answer)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
