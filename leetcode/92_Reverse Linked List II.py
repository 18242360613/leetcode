class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        i,last,pre,dummy.next = 1,None,dummy,head
        while head and i<=n:
            tmp = head.next
            if m<=i :
                if i==m:
                    last = head
                head.next = pre.next
                pre.next = head
            elif i == m-1:
                pre = head
            head = tmp
            i+=1
        last.next = head
        return dummy.next

