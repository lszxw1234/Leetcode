# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val + l2.val < 10:
            l3 = ListNode(l1.val + l2.val)
            l3.next = self.addTwoNumbers(l1.next, l2.next)
        else:
            l3 = ListNode(l1.val + l2.val - 10)
            tmp = ListNode(1)
            l3.next = self.addTwoNumbers(l1.next, self.addTwoNumbers(tmp, l2.next))
        return l3
