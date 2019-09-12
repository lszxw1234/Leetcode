# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        head1,head2=dummy,dummy

        for i in range(n):
            head1 = head1.next

        while head1.next:
            head1 = head1.next
            head2 = head2.next
        head2.next = head2.next.next

        return dummy.next
