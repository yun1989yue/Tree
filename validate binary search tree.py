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
