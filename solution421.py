class Solution:
    def fizzBuzz(self, n: int) -> list[str]:

        answer: list = []

        for number in range(1, n+1):
            if number % 3 == 0 and number % 5 == 0:
                answer.append("FizzBuzz")
            elif number % 3 == 0:
                answer.append("Fizz")
            elif number % 5 == 0:
                answer.append("Buzz")
            else:
                str_num = str(number)
                answer.append(str_num)

        return answer


