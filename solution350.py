class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        if nums1 == nums2:
            return nums1

        ans = []
        for i in nums1:
            if i in nums2:
                ans.append(i)
                nums2.remove(i)
        return ans




import solution350

if __name__ == '__main__':

    solution350 = solution350.Solution()

    answer = solution350.intersect([1, 2, 2, 1 ], [2, 2])
    print(answer)

    answer = solution350.intersect([2,2], [2,2])
    print(answer)


    answer = solution350.intersect([2], [2,2])
    print(answer)

