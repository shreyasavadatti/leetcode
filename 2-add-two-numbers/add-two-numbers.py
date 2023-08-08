# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        d=ListNode(0)
        ptr=d
        c=0
        while l1 or l2 or c:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + c
            c = total // 10
            ptr.next = ListNode(total % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            ptr = ptr.next

        return d.next
