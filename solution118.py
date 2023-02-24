class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        pascal_triangle = []

        for rows, numbers in enumerate(pascal_triangle):
            rows = numRows

        return pascal_triangle

    import solution118

    if __name__ == '__main__':
        solution118 = solution118.Solution()

        answer = solution118.generate(5)
        print(answer)