'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.
'''
'''
Method1: recursion O(n) time O(n) space
Use inorder traversal, and find the case(s) nums[i] > nums[i+1], if two adjacent numbers are swapped, then just 1 case
'''
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.pre = None
        self.helper(root)
        key = self.first.val
        self.first.val = self.second.val
        self.second.val = key
        
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.first:
                self.first = self.pre
            self.second = root
        self.pre = root
        self.helper(root.right)
'''
Morris O(n) time O(1) space
'''
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        pre = None
        cur = root
        while cur:
            if cur.left:
                rightMost = cur.left
                while rightMost.right and rightMost.right != cur:
                    rightMost = rightMost.right
                if rightMost.right:
                    rightMost.right = None
                    if pre and pre.val > cur.val:
                        if not first:
                            first = pre
                        second = cur
                    pre = cur
                    cur = cur.right
                else:
                    rightMost.right = cur
                    cur = cur.left
            else:
                if pre and pre.val > cur.val:
                    if not first:
                        first = pre
                    second = cur # attention!!! if two adjacent nodes(inorder traversal) exchanged, both nodes will be found, need to update second node
                pre = cur
                cur = cur.right
        key = first.val
        first.val = second.val
        second.val = key
