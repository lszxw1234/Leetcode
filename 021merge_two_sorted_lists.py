# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        res = ListNode(0)
        head = res
        while l1 and l2:
            if l1.val >= l2.val:
                res.next = l2
                l2 = l2.next

            else:
                res.next = l1
                l1 = l1.next
            res = res.next

        if l2:
            res.next = l2
        if l1:
            res.next = l1
        return head.next