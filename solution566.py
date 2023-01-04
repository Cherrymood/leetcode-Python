class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:


        list_nums = []
        answer = []

        for raw in mat:
            for column in raw:
                list_nums.append(column)

        x = len(list_nums)
        y = r * c

        if y != x:
            return mat
        else:
            for raw_index in range(r):
                answer.append(list_nums[(raw_index * c): (raw_index * c + c)])

        return answer










