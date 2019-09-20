# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1 or not head.next:
            return head

        cnt, pre, cur, nex = 1, None, head, head.next
        p = head

        while p:
            cnt += 1
            p = p.next
        if cnt - 1 >= k:
            cnt = 1
            while cnt < k and nex:
                cnt += 1
                cur.next = pre
                pre = cur
                cur = nex
                nex = nex.next
            cur.next = pre
        else:
            return cur

        if nex:
            head.next = self.reverseKGroup(nex, k)
        return cur


