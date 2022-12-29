class Solution:
    def average(self, salary: list[int]) -> float:

        sorted: list = salary.sort()
        length: int = len(salary)
        answer = (sum(salary)- salary[0] -salary[-1]) / (length-2)

        return answer