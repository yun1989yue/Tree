'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.current = root
        while self.current: # find the smallest value
            self.stack.append(self.current)
            self.current = self.current.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        self.current = self.stack.pop()
        res =  self.current.val
        self.current = self.current.right
        while self.current: # find next smallest value
            self.stack.append(self.current)
            self.current = self.current.left
        return res
