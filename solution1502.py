class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:

        arr.sort()

        check = arr[1] - arr[0]

        counter = 0

        for index in range(len(arr)-1):

            a = arr[index+1] - arr[index]
            if check == a:
                continue
            else:
                counter += 1
                break

        if counter == 1:
            return False
        else:
            return True




