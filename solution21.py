# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):

        if list1 == []:
            return list2
        elif list2  == []:
            return list1
        elif list1 == [] and list2 == []:
            return list1

        list3 = sorted((list1+list2))
        return list3






