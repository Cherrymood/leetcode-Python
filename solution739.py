class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        result = [0] * len(temperatures)
        stack = []
        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                current = stack.pop()
                result[current] = index - current
            stack.append(index)
        return result


    import solution739

    if __name__ == '__main__':
        solution739 = solution739.Solution()

        answer = solution739.dailyTemperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78])
        print(answer)

        answer = solution739.dailyTemperatures([73,74,75,71,69,72,76,73])
        print(answer)
