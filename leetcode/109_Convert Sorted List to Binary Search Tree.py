# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def build_tree(self,head,tail):
        if head==tail: return None
        fast,slow = head,head
        while fast!=tail and fast.next!=tail:
            fast = fast.next.next
            slow=slow.next

        root = TreeNode(slow.val)
        root.left = self.build_tree(head,slow)
        root.right = self.build_tree(slow.next,tail)
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return None
        return self.build_tree(head,None)

s = Solution()
# [-10,-3,0,5,9]
head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)
