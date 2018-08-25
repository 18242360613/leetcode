# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummyhead = ListNode(-float("inf"))
        dummyhead.next = head
        cur = head.next
        head.next = None
        while cur :
            next = cur.next
            start = dummyhead
            while start.next and start.next.val < cur.val:
                start = start.next

            if not start.next:
                start.next = cur
                cur.next = None
            else:
                cur.next = start.next
                start.next = cur
            cur = next
        return dummyhead.next

head = ListNode(4)
head.next = ListNode(2)
s = Solution()
ans = s.insertionSortList(head)
print(ans)