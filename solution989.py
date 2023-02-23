class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:

        if len(num) == 0:
            return k

        power: int = len(num)
        number: int = k
        answer: list[int] = []

        for index in range(len(num)):
            number += num[index] * 10**(power - (index+1))

        while number > 0:
            nums = number % 10
            answer.append(nums)
            number = number // 10

        return answer[::-1]

    import solution989
    if __name__ == '__main__':
        solution989 = solution989.Solution()
        answer = solution989.addToArrayForm([1, 2, 0, 0], 34)
        print(answer)

        answer = solution989.addToArrayForm([2, 7, 4], 181)
        print(answer)