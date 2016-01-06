'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''
'''
method: recursion O(n^2) time O(n) space
'''
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.depth(root.left) - self.depth(root.right)) <= 1
        
    def depth(self, root): # return max depth of node
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
'''
Method: DFS O(n) time O(n) space, similar as postorder
Consider following case O(n) space required
    1
   / \
  2   3
     / \
    4   5
       / \
      6   7
         / \
        8   9
'''
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.explore(root) != -1
        
    def explore(self, root):
        if not root:
            return 0
        leftDepth = self.explore(root.left) 
        if leftDepth == -1:
            return -1
        rightDepth = self.explore(root.right)
        if rightDepth == -1:
            return -1
        if abs(leftDepth - rightDepth) > 1:
            return -1
        return max(leftDepth, rightDepth) + 1
