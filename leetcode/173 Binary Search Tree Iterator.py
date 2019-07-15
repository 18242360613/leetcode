# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.index = 0
        self.inorder = []
        self.traverse(root)

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        self.inorder.append(root.val)
        self.traverse(root.right)


    def next(self) -> int:
        """
        @return the next smallest number
        """
        value = self.inorder[self.index]
        self.index = self.index + 1
        return value

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if len(self.inorder) > self.index else False

# class BSTIterator:
#
#     def __init__(self, root):
#         self.stack = list()
#         self.pushAll(root)
#
#     def next(self) -> int:
#         """
#         @return the next smallest number
#         """
#
#         node = self.stack.pop()
#         self.pushAll(node.right)
#         return node.val
#
#
#
#     def hasNext(self) -> bool:
#         """
#         @return whether we have a next smallest number
#         """
#         return True if len(self.stack) else False
#
#     def pushAll(self,node):
#         if node is not None:
#             self.stack.append(node)
#             self.pushAll(node.left)

node = TreeNode(7)
node.left = TreeNode(3)
node.right = TreeNode(15)
node.right.left = TreeNode(9)
node.right.right = TreeNode(20)

iterator = BSTIterator(node);
print(iterator.next());    # return 3
print(iterator.next());    # return 7
print(iterator.hasNext()); # return true
print(iterator.next());    # return 9
print(iterator.hasNext()); # return true
print(iterator.next());    # return 15
print(iterator.hasNext()); # return true
print(iterator.next());    # return 20
print(iterator.hasNext()); # return false

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()