class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        answer = []

        for index, num in list(enumerate(nums1)):
            ind = nums2.index(num)
            flag = False
            for index1 in range(ind+1, len(nums2)):
                if nums2[index1] > num:
                    answer.append(nums2[index1])
                    flag = True
                    break
            if not flag:
                answer.append(-1)

        return answer
