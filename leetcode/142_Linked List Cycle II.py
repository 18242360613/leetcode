# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast,slow,loop = head,head,False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                loop = True
                break

        if not loop:
            return None

        fast = head
        while fast!=slow:
            fast = fast.next
            slow = slow.next
        return fast