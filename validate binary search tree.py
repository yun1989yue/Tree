'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
'''
Method:
recursion O(n) time O(n) space
'''
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(-float('Inf'), root, float('Inf'))
        
    def helper(self, minN, root, maxN): # minN is lower bound of all the nodes of root, maxN is upper bound
        if not root:
            return True
        if root.val >= maxN or root.val <= minN: 
            return False
        if not root.left and not root.right:
            return True
        else:
            return self.helper(minN, root.left, min(root.val, maxN)) and self.helper(max(minN, root.val), root.right, maxN) 
'''
M2:
Get inorder traversal in stack, and judge whether it is increasing 
'''
'''
M3: inorder recursion O(n) time O(logn) space
'''
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.pre = None # reason for self.pre is if pre is parameter, it comes from upper level, but it should come from lower level
        self.res = True
        self.explore(root) 
        return self.res
        
    def explore(self, root):
        if not root:
            return
        self.explore(root.left)
        if self.pre and self.pre.val >= root.val:
                self.res = False
        self.pre = root
        self.explore(root.right)
        
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.pre = None
        return self.explore(root)
        
    def explore(self, root):
        if not root:
            return True
        if not self.explore(root.left):
            return False
        if self.pre and self.pre.val >= root.val:
                return False
        self.pre = root
        if not self.explore(root.right):
            return False
        return True
