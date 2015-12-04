'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''
'''
Method: recursion O(n) time O(logn) space but destroy the original tree
'''
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root)
        return self.res
        
    def helper(self, root):
        if not root:
            return
        if not root.left and not root.right:
            self.res += root.val
        if root.left:
            root.left.val += 10 * root.val
            self.helper(root.left)
        if root.right:
            root.right.val += 10 * root.val
            self.helper(root.right)
'''
Method: improved recursion 
'''
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root, 0)
        return self.res
        
    def helper(self, root, pre): # pre is number of upper nodes
        if not root:
            return
        current = pre * 10 + root.val
        if not root.left and not root.right:
            self.res += current
        if root.left:
            self.helper(root.left, current)
        if root.right:
            self.helper(root.right, current)
