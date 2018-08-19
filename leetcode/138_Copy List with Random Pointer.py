# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        nodedict,dummy,headclone = {},head.next, RandomListNode(head.label)
        nodedict[head] = headclone
        prenode = headclone

        while dummy:
            node = RandomListNode(dummy.label)
            prenode.next = node
            nodedict[dummy] = node
            prenode = node
            dummy = dummy.next

        dummy = headclone
        while head:
            dummy.random = nodedict.get(head.random)
            head = head.next
            dummy = dummy.next

        return headclone
