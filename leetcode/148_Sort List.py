# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge(self,first,second):
        dummy = ListNode(0)
        clone = dummy
        while first and second:
            if first.val <= second.val:
                clone.next = first
                first = first.next
            else:
                clone.next = second
                second = second.next
            clone = clone.next
        if first:
            clone.next = first
        if second:
            clone.next = second
        return dummy.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fast,second = head,head
        prev = head
        while fast and fast.next:
            fast = fast.next.next
            prev = second
            second = second.next
        prev.next = None
        head = self.sortList(head)
        second = self.sortList(second)
        return self.merge(head,second)

# 4->2->1->3

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

s = Solution()
head = s.sortList(head)
while head:
    print(head.val)
    head = head.next