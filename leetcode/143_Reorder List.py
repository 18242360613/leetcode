# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:return
        fast,slow = head,head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        middle = slow.next
        slow.next  = None
        while middle:
            tmp = middle.next
            middle.next = slow.next
            slow.next = middle
            middle = tmp
        fast = head

        while fast!=slow:
            tmp = slow.next
            slow.next = slow.next.next
            tmp.next = fast.next
            fast.next = tmp
            fast = fast.next.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

s = Solution()
s.reorderList(head)
while head:
    print(head.val)
    head = head.next